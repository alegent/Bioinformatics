##Approximate Pattern Matching Problem
#We say that position i in k-mers p1 ... pk and q1 ... qk is a mismatch if pi != qi. For example, CGAAT and CGGAC have two mismatches.

#Approximate Pattern Matching Problem
#Find all approximate occurrences of a pattern in a string.
#Given: Strings Pattern and Text along with an integer d.
#Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

#Sample Dataset
'''
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3
'''
#Sample Output
'''
6 7 26 27 78
'''
##########################################################################################

import os, sys, time

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_1f_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_1f_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
Pattern = (values[0])
DNA_seq = values[1]
d = int(values[2])
#Pattern = 'ATTCTGGA'
#DNA_seq = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
#d = 3
print Pattern
print DNA_seq
print d

k = len(Pattern)
k_mers = k - 1
iter = -1
ciclo = -1
print k

for Nucleotide in list(DNA_seq):
	ciclo += 1
	iter += 1
	k_mers += 1
	sequence = (DNA_seq)[iter:k_mers]
	Mismatch = 0
	number = -1
	#print sequence, ' = ', Pattern
	if len(sequence) == len(Pattern):
		#print len(sequence), ' = ', len(Pattern)
		for B in Pattern:
			number += 1
			if sequence[number] == Pattern[number]:
				Mismatch += 0
			else:
				Mismatch += 1
			#print sequence[number], Pattern[number]
		#print 'Mismatch: ', Mismatch
		if Mismatch <= int(d):
			print 'Posizione: ', ciclo
			Out_filetext.write(str(ciclo)+'\n')
Out_filetext.close()

print '\nThe number of Nucleotides is ', ciclo+1
print 'The DNA_seq is composed by a length of ',len(DNA_seq),' nucleotides'
# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'
print 'End'
