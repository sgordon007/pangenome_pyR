from pybedtools import *
from pyfaidx import Fasta
import numpy as np
import subprocess, os, shutil, sys
import glob
from shutil import copyfile
import stat

def unout2table(unout):
    unout = open(unout, 'r')

    unoutprefix = unout[:unout.rfind('.')]
    o1 = unoutprefix + '.tab.txt'
    o1h = open(o1, 'w')
    for line in unout:
        if not '[' in line:
            lineList = (line.split()).rstrip()
            out_list = [lineList[3], lineList[6], lineList[7], lineList[11], lineList[12]]
            o1h.write('%s\t%s\t%s\t%d\t%d\n' % (out_list))
    o1h.close()

########## end of initial analysis

if __name__ == "__main__":
    unout2table(unout=str(sys.argv[1]))
