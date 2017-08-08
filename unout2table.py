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
            g1 = lineList1[2].rstrip('.')
            g2 = lineList1[5].split('\t')[0]
            print g1
            print g2

            # lineList2 = line.split('\t')
            # re.findall(r"[\w']+", DATA)

            # out_list = [lineList1[2], lineList1[5], lineList2[0], float(lineList2[4]), float(lineList2[5])]
            # print '\t'.join(map(lambda x: ' $' + str(x), out_list))
            # o1h.write('%s\t%s\t%s\t%d\t%d\n' % (out_list))
    o1h.close()

########## end of initial analysis

if __name__ == "__main__":
    unout2table(unout=str(sys.argv[1]))
