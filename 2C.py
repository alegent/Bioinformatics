##Generating Theoretical Spectrum Problem
#Generating Theoretical Spectrum Problem
#Generate the theoretical spectrum of a cyclic peptide.
#Given: An amino acid string Peptide.
#Return: Cyclospectrum(Peptide).

#Sample Dataset
'''
LEQN
'''
#Sample Output
'''
0 113 114 128 129 227 242 242 257 355 356 370 371 484
'''
##Author: Alessandro Gentile
##UpDated: 2013-11-22
##########################################################################################

import os, sys, time
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_2c.txt'					#'rosalind_2c_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_2c_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
AA_Sequence = values[0]
#AA_Sequence = 'LEQN'
print AA_Sequence

AA_length = len(AA_Sequence)
print AA_length

def mass_spectrometer(Sequence):
	
	H = 137
	Q = 128
	P = 97
	R = 156
	L = 113
	D = 115
	E = 129
	A = 71
	G = 57
	V = 99
	Y = 163
	S = 87
	C = 103
	W = 186
	F = 147
	N = 114
	K = 128
	T = 101
	I = 113
	M = 131
	
	Masses = 0
	for AA in Sequence:
		if AA == 'H':
			Mass = H
		if AA == 'Q':
			Mass = Q
		if AA == 'P':
			Mass = P
		if AA == 'R':
			Mass = R
		if AA == 'L':
			Mass = L
		if AA == 'D':
			Mass = D
		if AA == 'E':
			Mass = E
		if AA == 'A':
			Mass = A
		if AA == 'G':
			Mass = G
		if AA == 'V':
			Mass = V
		if AA == 'Y':
			Mass = Y
		if AA == 'S':
			Mass = S
		if AA == 'C':
			Mass = C
		if AA == 'W':
			Mass = W
		if AA == 'F':
			Mass = F
		if AA == 'N':
			Mass = N
		if AA == 'K':
			Mass = K
		if AA == 'T':
			Mass = T
		if AA == 'I':
			Mass = I
		if AA == 'M':
			Mass = M
		Masses += (Mass)
	return Masses
	#Out_filetext.write(str(Masses)+'\n')

L = AA_length
ciclo = 0
L_first = 0
L_last = L
newL_first = -L
newL_last = -1
Sequence = (AA_Sequence)[L_first:L_last]
print Sequence
result = mass_spectrometer(Sequence)
Out_filetext.write('0'+'\n'+str(result))
print 'end of the ciclo', ciclo, 'L=', L

while L >= 1:# and ciclo < 3:
	ciclo +=1
	L = L-1
	L_first = 0
	L_last = L
	newL_first = -AA_length #-13
	newL_last = -AA_length+1
	print newL_last
	#print newL_first, newL_last
	for AA in AA_Sequence:
		Sequence = (AA_Sequence)[L_first:L_last]
		if len(Sequence) == L and len(Sequence) != 0:
			print Sequence
			result = mass_spectrometer(Sequence)
			Out_filetext.write('\n'+str(result))
			print result
		if len(Sequence) < L and len(Sequence) != 0:
			Sequence = (AA_Sequence)[L_first:L_last]+(AA_Sequence)[newL_first:newL_last]
			print Sequence
			result = mass_spectrometer(Sequence)
			Out_filetext.write('\n'+str(result))
			print result
			newL_last += +1
		L_first += +1
		L_last += +1
	print 'end of the ciclo', ciclo, 'L=', L
	newL_first = -L
	newL_last = -L+1
	
print '\nThe number of cicles is ', ciclo
print 'The Genome is composed by a length of ',len(AA_Sequence),' nucleotides'
# show elapsed time
endTime = time.time()
print 'Entire Genome elapsed time: ', endTime - startTime, ' seconds'
print 'End'
