import numpy as np
import subprocess, os, shutil, sys
import glob
from shutil import copyfile
import stat

def unout2table(unout):
    f = unout.rstrip()
    outFileName = f[:f.rfind('.')]+'.tab.txt'
    input = open(f, 'r')
    o1h = open(outFileName, 'w')
    for line in input:
        if not '[' in line:
            lineList = line.rstrip().split()
            out_list = [lineList[2], lineList[5], lineList[6], lineList[10], lineList[11]]
            o1h.write('%s\t%s\t%s\t%d\t%d\n' % (out_list))
    o1h.close()

########## end of initial analysis

if __name__ == "__main__":
    unout2table(unout=str(sys.argv[1]))
