import numpy as np
import sys
import Bio
from Bio import SeqIO

print(sys.argv[1])
matrixfile = open(sys.argv[1], 'r')
aaList = matrixfile.readline().split()
mafile = sys.argv[1]
n = len(aaList)
data = np.loadtxt(mafile, dtype = 'float', delimiter='\t', skiprows = 1, usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

resultsfile = open('sbpwiseresults.txt', 'w')

rec = list(open(sys.argv[2], 'r'))
records = []
for line in rec:
    records.append(line.strip())

for p in range(len(records)):
    for sequ in range(p+1, (len(records))):
        sumdist = 0 
        for i in range (min(len(records[p]), len(records[sequ]))):
            char_a = (records[p])[i]
            char_b = (records[sequ])[i]
            pos1 = aaList.index(char_a)
            pos2 = aaList.index(char_b)
                            #print(pos1)
                            #print(pos2)
            v = data[pos1, pos2]
                            #print(v)
            sumdist = sumdist + v
            avedist = sumdist/(len(records[sequ]))
        resultsfile.write( (records[p]) + '_' + (records[sequ]) + '\t' + repr(avedist) + '\n')
                                #print(sequ.id)
                                #print(secondseq.id)
                                #print(avedist)
resultsfile.close()


