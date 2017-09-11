import numpy as np
import subprocess, os, shutil, sys
import glob
from shutil import copyfile
import stat
import re
from collections import defaultdict

import re
import sys
import glob

for arg in sys.argv[2:]:
    for file in glob.iglob(arg):
        for line in open(file, 'r'):
            if re.search(sys.argv[1], line):
                print line,





e = sys.argv[1:]
counter = 1
fastaCorrespond = defaultdict(list)
os.mkdir('v0')
for file in os.listdir('.'):
    if file.endswith('.fa'):
        os.mkdir('v0/%s_%s_v0'%(e[0],'0'* (3-len(str(counter)))+ str(counter)))
        shutil.move(file,'v0/%s_%s_v0/%s_%s_v0.fa'%(e[0],'0'* (3-len(str(counter)))+ str(counter),e[0],'0'* (3-len(str(counter)))+ str(counter)))
        fastaCorrespond[file] = '%s_%s_v0.fa'%(e[0],'0'* (3-len(str(counter)))+ str(counter))
        counter += 1

with open('CorrespondenceAssemblies.txt','w') as f:
    f.write('\n'.join(original+'\t'+fastaCorrespond[original] for original in fastaCorrespond.keys()))


# open a list of fastq ids, then iterate through the list (for fastq in fastqlist)
# if the fastq is in the dictionary of the other tables then print the line for the tables
def merge_tables(ids, libraries, table2):
    outFileName = 'merged_table.tab.txt'
    ids = ids.strip()
    f1 = libraries.rstrip()

    for id in ids:
        for file in glob.iglob(arg):
            for line in open(file, 'r'):
                if re.search(sys.argv[1], line):
                    print line,
    input1 = open(f1, 'r')
    o1h = open(outFileName, 'w')
    dict1 = []
    dict2 = []
    for line in f1:


        if not '[' in line:
            line = line.strip()
            lineList1 = line.split()
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
    merge_tables(libraries=str(sys.argv[1]), table2=str(sys.argv[2]), ids=str(sys.argv[3]))
