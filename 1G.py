##Frequent Words with Mismatches Problem
#We defined a mismatch in "Approximate Pattern Matching Problem". We now generalize "Frequent Words Problem" to incorporate mismatches as well.

#Frequent Words with Mismatches Problem
#Find the most frequent k-mers with mismatches in a string.
#Given: A string Text as well as integers k and d.
#Return: All most frequent k-mers with up to d mismatches in Text.

#Note: The algorithm for solving the Frequent Words with Mismatches Problem becomes rather slow as k and d increase. In practice, your solution should work for k <= 12 and d <= 3.

#Sample Dataset
'''
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1
'''
#Sample Output
'''
GATG ATGC ATGT
'''
##########################################################################################

import os, sys, time

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'input.txt'					#'rosalind_1g_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_1g_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
DNA_seq = values[0]
k = int(values[1])	#4#
d = int(values[2])	#1#
#DNA_seq = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
print DNA_seq
print k
print d

DNA_lenght = len(DNA_seq)
#print DNA_lenght

Pattern_list = []
k_mers = k - 1
iter = -1
ciclo = -1
for N_1 in range(DNA_lenght):
	ciclo += 1
	iter += 1
	k_mers += 1
	sequence_k = (DNA_seq)[iter:k_mers]
	if len(sequence_k) == k:
		a = -1
		b = k - 1
		N_sequence = 0
		for N_2 in range(DNA_lenght):
			a += 1
			b += 1
			sequence = (DNA_seq)[a:b]
			Mismatch = 0
			number = -1
			if len(sequence) == len(sequence_k):
				#print sequence_k, ' = ', sequence
				#print len(sequence), ' = ', len(sequence_k)
				for B in sequence_k:
					number += 1
					if sequence_k[number] == sequence[number]:
						Mismatch += 0
					else:
						Mismatch += 1
					#print sequence[number], sequence_k[number]
				#print 'Mismatch: ', Mismatch
				if Mismatch <= d:
					#print 'Pattern: ', sequence_k
					#if sequence_k not in Pattern_list:
					Pattern_list += [sequence_k]
for Seq in Pattern_list:
	Out_filetext.write(Seq+'\n')
Out_filetext.close()

print '\nThe number of Nucleotides is ', ciclo+1
print 'The DNA_seq is composed by a length of ',len(DNA_seq),' nucleotides'
# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'
print 'End'
'''
NN = 'ACGT'

loop = 0
lista=[]
Sequence = ''
for N1 in NN:
	Sequence += N1
	#print Sequence
	
	for N2 in NN:
		Sequence += N2
		#print Sequence
		
	for N3 in NN:
		Sequence += N3
		
	for N4 in NN:
		name1 = Sequence+'A'
		name2 = Sequence+'C'
		name3 = Sequence+'G'
		name4 = Sequence+'T'
		lista = name1 +' '+ name2 +' '+ name3 +' '+ name4
		print lista
		
		stop

'''