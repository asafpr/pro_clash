#!/usr/bin/env python

"""
Read the list of chimeric interactions and generate a file that can be read
by circos.
"""

import sys
import argparse

def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object, replace the description
    parser = argparse.ArgumentParser(description='Generate circos data file.')

    settings = parser.parse_args(argv)

    return settings

def main(argv=None):
    settings = process_command_line(argv)
    # application code here, like:
    # run(settings, args)
    return 0        # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)
