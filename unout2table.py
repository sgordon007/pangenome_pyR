import numpy as np
import subprocess, os, shutil, sys
import glob
from shutil import copyfile
import stat
import re

def unout2table(unout):
    f = unout.rstrip()
    outFileName = f[:f.rfind('.')]+'.tab.txt'
    input = open(f, 'r')
    o1h = open(outFileName, 'w')
    for line in input:
        if not '[' in line:
            line = line.strip()
            lineList1 = line.split(',')
            g1 = lineList1[2]
            g1pre = g1[:re.search('.\d$', g1).start()]
            g2 = lineList1[5].split('\t')[0]
            lineList2 = line.split('\t')
            query = lineList2[1].split(':')[0]
            bait = lineList2[1].split(':')[1]
            # print g1
            # print g1pre
            # print g2
            out_list = [g1pre, g2, query, bait, float(lineList2[4]), float(lineList2[5])]
            o1h.write('\t'.join(map(lambda x: str(x), out_list)) + '\n')
    o1h.close()

########## end of initial analysis

if __name__ == "__main__":
    unout2table(unout=str(sys.argv[1]))
