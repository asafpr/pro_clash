#!/usr/bin/env python

"""
Using the summary file (generated by pro_clash_significant_regions.py) to
generate two lists of sequences, for the 5' end of the reads and the 3' ends.
Pad the sequences from both ends in a pre-determined length (default 20) and
if two regions overlap print only one (the first one - we're greedy)
"""

import sys
import argparse
import csv

from pro_clash import ecocyc_parser

def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object, replace the description
    parser = argparse.ArgumentParser(
        description='Generate sequences files of binding regions',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'summary_file',
        help='An output file of pro_clash_significant_regions.py.')
    parser.add_argument(
        'ec_dir',
        help='A EcoCyc dir of the bacteria.')
    parser.add_argument(
        'outhead',
        help='Output file starts with this, ends with _1.fa, _2.fa')
    parser.add_argument(
        '-p', '--pad', type=int, default=20,
        help='Pad the sequences from both sides with this length.')

    settings = parser.parse_args(argv)

    return settings


def read_summary_file(sfile, genome, pad):
    """
    Read the summary file, return the sequences.
    Arguments:
    - `sfile`: A summary file
    - `genome`: A dict from chr->Seq object
    - `pad`: add this length to each region
    """
    # Reported positions
    reported_as_1 = {'+': set(), '-': set()}
    reported_as_2 = {'+': set(), '-': set()}
    # Returned sequences name -> seq
    ret_seqs_1 = {}
    ret_seqs_2 = {}
    for line in csv.DictReader(open(sfile), delimiter='\t'):
        r1_from = int(line['RNA1 from'])-1
        r1_to = int(line['RNA1 to'])
        r1_chrn = line['RNA1 chromosome']
        r1_str = line['RNA1 strand']
        r2_from = int(line['RNA2 from'])-1
        r2_to = int(line['RNA2 to'])
        r2_chrn = line['RNA2 chromosome']
        r2_str = line['RNA2 strand']
        if len(reported_as_1[r1_str] & set(range(r1_from, r1_to))) == 0:
            # Report region 1
            retseq = genome[r1_chrn][r1_from-pad:r1_to+pad]
            if r1_str == '-':
                retseq = retseq.reverse_complement()
            ret_seqs_1['_'.join(
                    [str(h) for h in [r1_chrn, r1_from, r1_to, r1_str]])] = retseq
            for i in range(r1_from-pad, r1_to+pad):
                reported_as_1[r1_str].add(i)
        if len(reported_as_2[r2_str] & set(range(r2_from, r2_to))) == 0:
            # Report region 1
            retseq = genome[r2_chrn][r2_from-pad:r2_to+pad]
            if r2_str == '-':
                retseq = retseq.reverse_complement()
            ret_seqs_2['_'.join(
                    [str(h) for h in [r2_chrn, r2_from, r2_to, r2_str]])] = retseq
            for i in range(r2_from-pad, r2_to+pad):
                reported_as_2[r2_str].add(i)
    return ret_seqs_1, ret_seqs_2
            

def main(argv=None):
    settings = process_command_line(argv)
    fsas = ecocyc_parser.read_fsas(settings.ec_dir)
    ret_seqs1, ret_seqs2 = read_summary_file(
        settings.summary_file, fsas, settings.pad)
    with open("%s_1.fa"%settings.outhead, 'w') as out1:
        for k, v in ret_seqs1.items():
            out1.write(">%s\n%s\n"%(k, v))
    with open("%s_2.fa"%settings.outhead, 'w') as out2:
        for k, v in ret_seqs2.items():
            out2.write(">%s\n%s\n"%(k, v))
    
    # application code here, like:
    # run(settings, args)
    return 0        # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)