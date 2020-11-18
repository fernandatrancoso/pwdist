# pwdist
My first script!! 


pwdist: Script to calculate average pairwise distance between peptide sequences based on a distance matrix and a fasta file. 
filepwdist: Same but comparing peptides of one file to peptides of another file.

Based on this program (https://sourceforge.net/projects/granthamdist/) made by Tobias Lenz. 

pwdist usage: > python3 pwisedist.py distancematrix.txt fastafile 

filepwdist usage: > python3 filepwdist.py distancematrixfile fastafile1 fastafile2

!!!To run you must have python3, numpy, and biopython installed. 

!!!The peptide sequences must have THE SAME LENGTH

!!!If your matrix has more than 20 amino acids, change usecols to accomodate the max number of columns of your distance matrix. delimiter should be '\t' 

outputfile is "resultsfile.txt", it will give you the ids of the compared sequences and the average pairwise distance between the compared sequences 

Please let me know if you find any errors :)
