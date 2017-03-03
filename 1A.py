##Frequent Words Problem
#This is the first problem in a collection of "code challenges" to accompany Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
#A k-mer is a string of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text. For example,
#Count(ACAACTATGCATACTATCGGGAACTATCCT,ACTAT)=3.
#We note that Count(CGATATATCCATAG, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.
#We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

#Frequent Words Problem
#Find the most frequent k-mers in a string.
#Given: A DNA string Text and an integer k.
#Return: All most frequent k-mers in Text (in any order).

#Sample Dataset
'''
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
'''
#Sample Output
'''
CATG GCAT
'''
##########################################################################################

import os, time
from Bio.Seq import Seq

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'input.txt'	#'rosalind_1a_2_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'	#'rosalind_1a_2_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
DNA_seq = values[0]
k = int(values[1])	#4#
#DNA_seq = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
print DNA_seq
print k

DNA_seq_list = list(DNA_seq)
#print DNA_seq_list
DNA_lenght = len(DNA_seq)
#print DNA_lenght

sequence_k_selection = ()
sequence_k_list = []
max_N_sequence = 0
k_mers = k - 1
iter = -1
for N_1 in range(DNA_lenght):
	iter += 1
	k_mers += 1
	sequence_k = (DNA_seq)[iter:k_mers]
	#print N_1, iter, k_mers, sequence_k
	if len(sequence_k) == k:
		a = -1
		b = k - 1
		N_sequence = 0
		for N_2 in range(DNA_lenght):
			a += 1
			b += 1
			sequence = (DNA_seq)[a:b]
			if sequence_k == sequence:
				N_sequence += 1
				#print N_sequence, sequence, ' = ', sequence_k
		if N_sequence >= max_N_sequence:
			max_N_sequence = N_sequence
			#print 'max_N_sequence -->', max_N_sequence
				
		if N_sequence >= max_N_sequence:
			#sequence_k_selection = (str(N_sequence)+' '+sequence_k)
			#print sequence_k_selection
			sequence_k_list.insert(0,str(N_sequence))
			sequence_k_list.insert(1,sequence_k)
print sequence_k_list

seq_list = []
max_value = int(sequence_k_list[0])
print 'max_value is ',max_value
n = 0
for iter in range(len(sequence_k_list)/2):
	N_sequence = int(sequence_k_list[n])
	sequence_k = sequence_k_list[n+1]
	n+=2
	if N_sequence >= max_value:
		max_value = N_sequence
		if sequence_k not in seq_list:
			seq_list += [sequence_k]
print seq_list
for seq in seq_list:
	Out_filetext.write(str(seq)+'\n')
Out_filetext.close()

# show elapsed time
endTime = time.time()
print 'Entire Genome elapsed time: ', endTime - startTime, ' seconds'

print 'end'
