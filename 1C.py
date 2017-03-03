##Pattern Matching Problem

#Recall from that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.
#Pattern Matching Problem
#Find all occurrences of a pattern in a string.

#Given: Strings Pattern and Genome.
#Return: All starting positions  in Genome where Pattern appears as a substring.

#Sample Dataset
'''
ATAT
GATATATGCATATACTT
'''
#Sample Output
'''
1 3 9
'''
##########################################################################################

import os, time
from Bio.Seq import Seq

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_1c_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'						#'rosalind_1c_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
Pattern = values[0]
DNA_seq = values[1]
#print Pattern
#print DNA_seq
#Pattern = 'ATAT'
#DNA_seq = 'GATATATGCATATACTT'


DNA_seq_list = list(DNA_seq)
DNA_lenght = len(DNA_seq)

k = len(Pattern)
k_mers = k - 1
iter = -1
ciclo = -1

for Nucleotide in DNA_seq_list:
	ciclo = ciclo + 1
	iter = iter + 1
	k_mers = k_mers + 1
	sequence = (DNA_seq)[iter:k_mers]
	if sequence == Pattern:
		print ciclo, ' '#, sequence, ' = ', Pattern
		Out_filetext.write(str(ciclo)+'\n')
Out_filetext.close()

# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'

print 'end'