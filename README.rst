================
PRO-CLASH
================
Intention
---------
This package can be used to analyzed PRO-CLASH experiments. It is written for a prokaryotic genome, without splice junction mapping and with some additional features. PRO-CLASH is described in <Insert citation> by Melamed *et al*.

The package handles the different stages processing fastq files to pairs of interacting RNAs and some statistics. It *does not* handle quality issues, adapter removing etc. so the fastq files should be treated with cutadapt or equivalent before applying this package.

Simple mapping
--------------
The first stage is to map the reads to the genome. In this readme file it's assumed that the reads are paired-end but all the commands will work for single-end mapping.

.. code-block:: console
map_and_count.py -g genome.fa -a annotations.gff -1 reads_1.fastq[.gz] -2 reads_2.fastq[.gz] -o output_head -n wiggle_name -d "wiggle description"
