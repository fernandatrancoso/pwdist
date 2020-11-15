# pwdist
My first script!!
Script to calculate average pairwise distance between peptide sequences based on a distance matrix and a fasta file
usage python3 pwisedist.py distancematrix.txt fastafile
if your matrix has more than 20 amino acids, change usecols to accomodate the max number of columns of your distance matrix. delimiter should be '\t'
outputfile is "resultsfile.txt", it will give you the ids of the compared sequences and the average pairwise distance between the compared sequences
Please let me know if you find any errors :)
