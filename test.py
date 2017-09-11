import re
import sys
import glob
from collections import defaultdict

#  python ./test.py distachyon_hybridum.fastq.ids.list combined.libraries_working.info CorrespondenceAssemblies.txt
dict = defaultdict(list)
fastq_files = open(sys.argv[1], 'r')
for fastq in fastq_files:
    fastq = fastq.strip()
    for arg in sys.argv[3:]:
        for file in glob.iglob(arg):
            for line in open(file, 'r'):
                if re.search(fastq, line):
                    dict[fastq].append(line.strip('\n'))
with open(sys.argv[2], 'w') as f:
    f.write('\n'.join(fastq + '\t' + "\t".join(str(x) for x in dict[fastq]) for fastq in dict.keys()))
