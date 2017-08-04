#!/usr/bin/env python

pan_matrix_f = '/Users/sgordon/Documents/distachyon50/pangenome_R/data/pangenome_matrix_t0.tab.rotated.txt'

def modclust_id(pan_matrix_f):
    """extract the gene id from bruno clust_id and make it the new clust_id"""
    f = pan_matrix_f.rstrip()
    outFileName = f[:f.rfind('.')]+'.shortid.txt'
    open(outFileName, 'w').close()
    outputFile = open(outFileName, 'w')
    inputFile = open(f, 'r')
    for line in inputFile:
        line = line.split()
        pref_id = line[0].rstrip('.fna')
        print pref_id
    inputFile.close()
    outputFile.close()

        # lineOutputList = [lineInList[1], int(lineInList[8]), int(lineInList[8])+1]
        # outputFile.write('%s\t%d\t%d\n' % tuple(lineOutputList))

modclust_id(pan_matrix_f)