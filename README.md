# pwdist
My first script!! \n
Script to calculate average pairwise distance between peptide sequences based on a distance matrix and a fasta file. \n
Based on this program (https://sourceforge.net/projects/granthamdist/) made by Tobias Lenz. \n
usage: > python3 pwisedist.py distancematrix.txt fastafile \n
To run you must have python3, numpy, and biopython installed. \n
if your matrix has more than 20 amino acids, change usecols to accomodate the max number of columns of your distance matrix. delimiter should be '\t' \n
outputfile is "resultsfile.txt", it will give you the ids of the compared sequences and the average pairwise distance between the compared sequences \n
Please let me know if you find any errors :)
