##Clump Finding Problem

#Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. For example, TGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAaTGCAtgacaagccTGCAgttgttttac.
#Clump Finding Problem
#Find patterns forming clumps in a string.

#Given: A string Genome, and integers k, L, and t.
#Return: All distinct k-mers forming (L, t)-clumps in Genome.

#Sample Dataset
'''
CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4
'''
#Sample Output
'''
CGACA GAAGA AATGT
'''
##########################################################################################


import os, time
from Bio.Seq import Seq

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_1d_2_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_1d_2_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
DNA_seq = values[0]
k = int(values[1])	#5#
L = int(values[2])	#75#
t = int(values[3])	#4#
#DNA_seq = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
print DNA_seq
print k
print L
print t

DNA_seq_list = list(DNA_seq)
DNA_lenght = len(DNA_seq)

frequency = t
ciclo = -1

L_first = 0
L_last = L
sequence_list = []
for OriC_Bases in range(DNA_lenght):
	OriC = (DNA_seq)[L_first:L_last]
	L_first = L_first + L
	L_last = L_last + L
	
	OriC_Length = len(OriC)
	if  OriC_Length <= L:
		#print OriC
		
		iter = -1
		k_mers = k - 1
		for Nucleotide in OriC:
			iter = iter + 1
			k_mers = k_mers + 1
			sequence_k = (OriC)[iter:k_mers]
			
			a = -1
			b = k - 1
			N_sequence = 0
			for N_mers in DNA_seq:
				a = a + 1
				b = b + 1
				sequence = (DNA_seq)[a:b]
				
				if sequence == sequence_k:
					N_sequence = N_sequence + 1
					if N_sequence >= frequency:
						#print N_sequence, sequence, ' = ', sequence_k
						if sequence not in sequence_list:
							sequence_list += [sequence]
							#print sequence_list

for sequence in sequence_list: 
	Out_filetext.write(sequence+'\n')
Out_filetext.close()

# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'
print 'The DNA_seq is composed by a length of ',len(DNA_seq),' nucleotides'

print 'end'
