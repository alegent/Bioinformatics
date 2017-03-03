##In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a string Pattern = p1...pn is the string Pattern = pn ... p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.
#For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

#Reverse Complement Problem
#Find the reverse complement of a DNA string.

#Given: A DNA string Pattern.
#Return: Pattern, the reverse complement of Pattern.

#Sample Dataset
'''
AAAACCCGGT
'''
#Sample Output
'''
ACCGGGTTTT
'''
##########################################################################################

import os, time
from Bio.Seq import Seq

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_1b_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'	#rosalind_1b_1_output
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

for line in lines:
	DNA_seq = line
#DNA_seq = 'AAAACCCGGT'
print DNA_seq
DNA_seq_list = list(DNA_seq)
#print DNA_seq_list
DNA_lenght = len(DNA_seq)
'''
# using the Bio.Seq module
DNA_seq = Seq('AAAACCCGGT')
DNA_revc = DNA_seq.reverse_complement()
print DNA_revc
'''
DNA_rev=''
DNA_revc=''
Base=''
i=DNA_lenght
for N in range(DNA_lenght):
	DNA_rev += DNA_seq_list[i-1]
	i+=-1
print DNA_rev

for Nucleotide in DNA_rev:
	if Nucleotide == 'A':
		Base = 'T'
	if Nucleotide == 'T':
		Base = 'A'
	if Nucleotide == 'C':
		Base = 'G'
	if Nucleotide == 'G':
		Base = 'C'
	DNA_revc += Base
print DNA_revc

Out_filetext.write(str(DNA_revc))
Out_filetext.close()

# show elapsed time
endTime = time.time()
print 'Entire Genome elapsed time: ', endTime - startTime, ' seconds'

print 'end'
