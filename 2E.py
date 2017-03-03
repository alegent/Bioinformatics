##Cyclopeptide Sequencing Problem
#Solve the Cyclopeptide Sequencing Problem
#Given an ideal experimental spectrum, find a cyclic peptide whose theoretical spectrum matches the experimental spectrum.
#Given: A collection of (possibly repeated) integers Spectrum corresponding to an ideal experimental spectrum.
#Return: An amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).

#Sample Dataset
'''
0 113 128 186 241 299 314 427
'''
#Sample Output
'''
186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
 '''
##Author: Alessandro Gentile
##UpDated: 2013-11-25
##########################################################################################

import os, sys, time
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'input.txt'					#'rosalind_2e_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_2e_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
Spectrum = values
#Spectrum = '0 113 128 186 241 299 314 427'
print Spectrum

S_length = len(Spectrum)
print S_length

def mass_spectrometer(Mass):
	Mass = int(Mass)
	G = 57
	A = 71
	S = 87
	P = 97
	V = 99
	T = 101
	C = 103
	I = 113
	L = 113
	N = 114
	D = 115
	K = 128
	Q = 128
	E = 129
	M = 131
	H = 137
	F = 147
	R = 156
	Y = 163
	W = 186
	'''
	def BFCyclopeptideSequencing(Masses):
		for peptide with Mass(Peptide) equal to ParentMass(Spectrum)
			if Spectrum = Cyclospectrum(Peptide)
				output Peptide
	'''
	if Mass == 57:
		AA = 'G'
	if Mass == 71:
		AA = 'A'
	if Mass == 87:
		AA = 'S'
	if Mass == 97:
		AA = 'P'
	if Mass == 99:
		AA = 'V'
	if Mass == 101:
		AA = 'T'
	if Mass == 103:
		AA = 'C'
	if Mass == 113:
		AA = '(LI)'
	#if Mass == 113:
	#	AA = 'L'
	if Mass == 114:
		AA = 'N'
	if Mass == 115:
		AA = 'D'
	if Mass == 128:
		AA = '(QK)'
	#if Mass == 128:
	#	AA = 'K'
	if Mass == 129:
		AA = 'E'
	if Mass == 131:
		AA = 'M'
	if Mass == 137:
		AA = 'H'
	if Mass == 147:
		AA = 'F'
	if Mass == 156:
		AA = 'R'
	if Mass == 163:
		AA = 'Y'
	if Mass == 186:
		AA = 'W'
	return AA

def mass_spectrometer2(Mass, N_AA):
	Mass = int(Mass)
	List_AA_Masses = [('G', 57), ('A', 71), ('S', 87), ('P', 97), ('V', 99), ('T', 101), ('C', 103), ('(IL)', 113), ('N', 114), ('D',	115), ('(KQ)', 128), ('E', 129), ('M', 131), ('H', 137), ('F', 147), ('R', 156), ('Y', 163), ('W', 186)]
	#List_AA_Masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
	N_Ciclo = 0
	'''
	while N_Ciclo <= N_AA
		N_Ciclo += 1
		for (AA, AA_Mass) in List_AA_Masses:
			summa += AA
	'''		
	for (AA1, AA_Mass1) in List_AA_Masses:
		#print AA1, AA_Mass1
		for (AA2, AA_Mass2) in List_AA_Masses:
			#print AA2, AA_Mass2
			AA_Mass = AA_Mass1 + AA_Mass2
			#print AA_Mass
			if Mass == AA_Mass:
				print 'si', Mass, '==', AA_Mass
				print 'the AA are: ', AA1+AA2
				return AA1+AA2

Masses = Spectrum
print Masses
for Mass in Masses[1:]:
	print Mass
S_length = len(Spectrum)

ciclo = 0
for Mass in Masses:
	List_AA = ''
	print ciclo
	ciclo += 1
	# Ciclo for one AA
	if int(Mass) > 0 and int(Mass) <= 186:
		variable = mass_spectrometer(Mass)
		print variable
		Out_filetext.write(variable)
		N_AA = ciclo-1
		print 'the number of AA is: ', N_AA
		List_AA += variable
	print List_AA
	'''
	# Ciclo for two AA
	if int(Mass) > 186 and int(Mass) <= 372:
		variable = mass_spectrometer2(Mass, N_AA)
		print variable
		Out_filetext.write(variable)
	# Ciclo for three AA
	if int(Mass) > 372 and int(Mass) <= 558:
		variable = mass_spectrometer2(Mass, N_AA)
		print variable
		Out_filetext.write(variable)
	# Ciclo for four AA
	if int(Mass) > 558 and int(Mass) <= 744:
		variable = mass_spectrometer2(Mass, N_AA)
		print variable
		Out_filetext.write(variable)
	# Ciclo for five AA
	if int(Mass) > 744 and int(Mass) <= 930:
		variable = mass_spectrometer2(Mass, N_AA)
		print variable
		Out_filetext.write(variable)
	'''
Out_filetext.close()
#print '\nThe number of cicles is ', ciclo
print 'The Genome is composed by a length of ',len(Spectrum),' nucleotides \n'
# show elapsed time
endTime = time.time()
print 'Entire Genome elapsed time: ', endTime - startTime, ' seconds'
print 'End'
