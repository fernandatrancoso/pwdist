##TESTE
import numpy as np
import sys
import Bio
from Bio import SeqIO


#usage pythonfile distancematrixfile fastafile
#aaDistanceMatrix = open(sys.argv[1], 'r')
#fastaFile = open(sys.argv[2], 'r')
print(sys.argv[1])
matrixfile = open(sys.argv[1], 'r')
aaList = matrixfile.readline().split()
mafile = sys.argv[1]
n = len(aaList)
data = np.loadtxt(mafile, dtype = 'float', delimiter='\t', skiprows = 1, usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

resultsfile = open('resultsfile.txt', 'w')

records = list(SeqIO.parse(open(sys.argv[2], 'r'), "fasta"))

for p in range(len(records)):
    for sequ in range(p+1, (len(records))):
        sumdist = 0 
        for i in range (min(len(records[p].seq), len(records[sequ].seq))):
            char_a = (records[p].seq)[i]
            char_b = (records[sequ].seq)[i]
            pos1 = aaList.index(char_a)
            pos2 = aaList.index(char_b)
                            #print(pos1)
                            #print(pos2)
            v = data[pos1, pos2]
                            #print(v)
            sumdist = sumdist + v
            avedist = sumdist/(len(records[sequ].seq))
        resultsfile.write( repr(records[p].id) + '_' + repr(records[sequ].id) + repr(avedist) + '\n')
                                #print(sequ.id)
                                #print(secondseq.id)
                                #print(avedist)
resultsfile.close()

