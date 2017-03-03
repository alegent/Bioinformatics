##Minimum Skew Problem
#Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of G and C in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are:
#0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

#Minimum Skew Problem
#Find a position in a genome minimizing the skew.
#Given: A DNA string Genome.
#Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

#Sample Dataset
'''
CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG
'''
#Sample Output
'''
53 97
'''
##########################################################################################

import os, sys, time


# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_1e_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_1e_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
DNA_seq = values[0]
#DNA_seq = 'CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'
print DNA_seq

ciclo = 0
skew = 0
skiew_list = []
skew_min = -1
for Nucleotide in list(DNA_seq):
	ciclo += 1
	if Nucleotide == 'C':
		skew += -1
	if Nucleotide == 'G':
		skew += 1
	if Nucleotide == 'A':
		skew += 0
	if Nucleotide == 'T':
		skew += 0
	#print 'ciclo: ', ciclo, ' Nucleotide: ', Nucleotide, ' skew: ', skew
	
	if skew <= skew_min:
		skew_min = skew
		#print 'ciclo: ', ciclo, ' Nucleotide: ', Nucleotide, ' skew: ', skew_min
		skiew_list.insert(0,str(skew_min))
		skiew_list.insert(1,str(ciclo))
print skiew_list

new_skiew_list = []
min_value = int(skiew_list[0])
print 'min_value is ',min_value
n = 0
for iter in range(len(skiew_list)/2):
	skiew_value = int(skiew_list[n])
	skiew_position = skiew_list[n+1]
	n+=2
	if skiew_value <= min_value:
		min_value = skiew_value
		if skiew_position not in new_skiew_list:
			new_skiew_list += [skiew_position]
print new_skiew_list

for skiew in new_skiew_list:
	Out_filetext.write(str(skiew)+'\n')
Out_filetext.close()

print '\nThe number of Nucleotides is ', ciclo+1
print 'The DNA_seq is composed by a length of ',len(DNA_seq),' nucleotides'
# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'
print 'End'