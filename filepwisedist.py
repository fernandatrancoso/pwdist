##TESTE
import numpy as np
import sys
import Bio
from Bio import SeqIO


#usage pythonfile distancematrixfile fastafile1 fastafile2
#aaDistanceMatrix = open(sys.argv[1], 'r')
#fastaFile1 = open(sys.argv[2], 'r')
#fastafile2 = open(sys.argv[3], 'r')
print(sys.argv[1])
matrixfile = open(sys.argv[1], 'r')
aaList = matrixfile.readline().split()
mafile = sys.argv[1]
n = len(aaList)
data = np.loadtxt(mafile, dtype = 'float', delimiter='\t', skiprows = 1, usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

resultsfile = open('filepwisedistresults.txt', 'w')

records = list(SeqIO.parse(open(sys.argv[2], 'r'), "fasta"))
records2 = list(SeqIO.parse(open(sys.argv[3], 'r'), "fasta"))
for line1 in range(len(records)):
    for sequ in range((len(records2))):
        sumdist = 0 
        for i in range (min(len(records[line1].seq), len(records2[sequ].seq))):
            char_a = (records[line1].seq)[i]
            char_b = (records2[sequ].seq)[i]
            pos1 = aaList.index(char_a)
            pos2 = aaList.index(char_b)
                            #print(pos1)
                            #print(pos2)
            v = data[pos1, pos2]
                            #print(v)
            sumdist = sumdist + v
            avedist = sumdist/(len(records[sequ].seq))
        resultsfile.write( repr(records[line1].id) + '_' + repr(records2[sequ].id) + repr(avedist) + '\n')
                                #print(sequ.id)
                                #print(secondseq.id)
                                #print(avedist)
resultsfile.close()

