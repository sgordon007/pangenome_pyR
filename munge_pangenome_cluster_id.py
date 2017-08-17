#!/usr/bin/env python
import re

pan_matrix_f = '/Users/sgordon/Documents/distachyon50/pangenome_R/data/pangenome_matrix_t0.tab.rotated.txt'
occur = 1

def modclust_id(pan_matrix_f):
    """extract the gene id from bruno clust_id and make it the new clust_id"""
    f = pan_matrix_f.rstrip()
    outFileName = f[:f.rfind('.')]+'.shortid.txt'
    open(outFileName, 'w').close()
    outputFile = open(outFileName, 'w')
    inputFile = open(f, 'r')
    for line in inputFile:
        line = line.split()
        # pref_id = line[0].rstrip('.fna')
        pref_id = line[0].rstrip('.fna')
        indices = [x.start() for x in re.finditer("_", pref_id)]
        # part1 = pref_id[0:indices[occur - 1]]
        part2 = pref_id[indices[occur - 1] + 1:]
        # lineOutputList = [part2, line[1:]]
        l1 = [part2]
        l2 = line[1:]
        l3 = l1 + l2
        out_string = '\t'.join(l3)
        outputFile.write('%s\n' % out_string)

    inputFile.close()
    outputFile.close()

modclust_id(pan_matrix_f)