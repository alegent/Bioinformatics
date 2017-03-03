##Peptide Encoding Problem
#Peptide Encoding Problem
#Find substrings of a genome encoding a given amino acid sequence.
#Given: A DNA string Text and an amino acid string Peptide.
#Return: All substrings of Text encoding Peptide (if any such substrings exist).

#Sample Dataset
'''
ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA
'''
#Sample Output
'''
ATGGCC
GGCCAT
ATGGCC
'''
##Author: Alessandro Gentile
##Dated: 2013-11-22
##LastUpDated: 2014-06-09
##########################################################################################

import os, sys, time
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'input.txt'					#'rosalind_2b_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_2b_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
DNA_seq = values[0]
Peptide = values[1]
DNA_seq = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
Peptide = 'MA'
print DNA_seq
print Peptide

DNA_lenght = len(DNA_seq)
#print DNA_lenght

'''MAMAPRTEINSTRING*
MA
*GNIRTSNIETRPAMAM
               AM

M = ['AUG']
A = ['GCU','GCC','GCA','GCG']

M  A   A  M
ATGGCT AGCCAT
ATGGCC GGCCAT
ATGGCA TGCCAT
ATGGCG CGCCAT
'''

L = len(Peptide)
RNA_seq = ''
for Nucleotide in list(DNA_seq):
	if Nucleotide == 'T':
		Nucleotide = 'U'
	RNA_seq += Nucleotide
print RNA_seq

messenger_rna = Seq(RNA_seq, IUPAC.unambiguous_rna)
protein = messenger_rna.translate()
print protein

'''
List_AminoAcid = ['H','Q','P','R','L','D','E','A','G','V','Y','Stop','S','C','W','F','N','K','T','I','M']
List_Codon = []
'''

def Peptide_Encoding(aa):
	H = ['CAU','CAC']
	Q = ['CAA','CAG']
	P = ['CCU','CCC','CCA','CCG']
	R = ['CGU','CGC','CGA','CGG','AGA','AGG']
	L = ['CUU','CUC','CUA','CUG','UUA','UUG']
	D = ['GAU','GAC']
	E = ['GAA','GAG']
	A = ['GCU', 'GCC', 'GCA', 'GCG']
	G = ['GCU','GCC','GCA','GCG']
	V = ['GUU','GUC','GUA','GUG']
	Y = ['UAU','UAC']
	Stop = ['UAA','UAG','UGA']
	S = ['UCU','UCC','UCA','UCG','AGU','AGC']
	C = ['UGU','UGC']
	W = ['UGG']
	F = ['UUU','UUC']
	N = ['AAU','AAC']
	K = ['AAA','AAG']
	T = ['ACU','ACC','ACA','ACG']
	I = ['AUU','AUC','AUA']
	M = ['AUG']
	codon_list = ''
	if aa == 'H':
		for codon in H:
			codon_list += codon
		return codon_list
	if aa == 'Q':
		for codon in Q:
			codon_list += codon
		return codon_list
	if aa == 'A':
		for codon in A:
			codon_list += codon
		return codon_list
	if aa == 'G':
		for codon in G:
			codon_list += codon
		return codon_list
	if aa == 'I':
		for codon in I:
			codon_list += codon
		return codon_list
	if aa == 'M':
		for codon in M:
			codon_list += codon
		return codon_list
'''
def Triplette_Comparison(RNA, value):
	for triplette in RNA:
'''	
ciclo = 0
seq_ini = 0
seq_last = L
for AA in protein:
	ciclo += 1
	sequence = (protein)[seq_ini:seq_last]
	if str(sequence) == str(Peptide):
		print 'yes ', sequence, ' == ', Peptide
		func_result = ''
		for aa in sequence:
			print aa
			codon_list_result = Peptide_Encoding(aa)
			print codon_list_result
			
			codon_ini = 0
			codon_last = 3
			for triplette in codon_list_result:
				codon = codon_list_result[codon_ini:codon_last]
				if len(codon) == 3:
					value = codon
					print value
					Triplette_Comparison(RNA, value)
				codon_ini += +3
				codon_last += +3
		
		
		#for DNA_Triplets in list(DNA):
		#codon1 = (RNA)[codon_ini:codon_last]
		#codon2 = (RNA)[codon_ini+3:codon_last+3]
		#print codon1, codon2
		
	seq_ini += 1
	seq_last += 1

	
	
'''
def Peptide_Encoding(codon, Peptide):
	Sequence = ''
	if codon == 'CAU' or codon == 'CAC':
		AA = 'H'
	if codon == 'CAA' or codon == 'CAG':
		AA = 'Q'
	if codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
		AA = 'P'
	if codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon ==  'AGA' or codon == 'AGG':
		AA = 'R'
	if codon == 'CUU' or codon ==  'CUC' or codon == 'CUA' or codon == 'CUG' or codon == 'UUA' or codon == 'UUG':
		AA = 'L'
	if codon == 'GAU' or codon == 'GAC':
		AA = 'D'
	if codon == 'GAA' or codon == 'GAG':
		AA = 'E'
	if codon == 'GCU' or codon == 'GCC' or codon ==  'GCA' or codon == 'GCG':
		AA = 'A'
	if codon == 'GGU' or codon == 'GGC' or codon ==  'GGA' or codon == 'GGG':
		AA = 'G'
	if codon == 'GUU' or codon == 'GUC' or codon ==  'GUA' or codon == 'GUG':
		AA = 'V'
	if codon == 'UAU' or codon == 'UAC':
		AA = 'Y'
	if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
		AA = '*'
	if codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
		AA = 'S'
	if codon == 'UGU' or codon == 'UGC':
		AA = 'C'
	if codon == 'UGG':
		AA = 'W'
	if codon == 'UUU' or codon == 'UUC':
		AA = 'F'
	if codon == 'AAU' or codon == 'AAC':
		AA = 'N'
	if codon == 'AAA' or codon == 'AAG':
		AA = 'K'
	if codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
		AA = 'T'
	if codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
		AA = 'I'
	if codon == 'AUG':
		AA = 'M'
	for AA_new in Peptide:
			if AA == Peptide[0:1]:
				print codon
			Sequence += AA
			print Sequence
	

ciclo = -1
iter = 0
k_mers = k
for RNA_Triplets in list(RNA):
	ciclo += 1
	codon = (RNA)[iter:k_mers]
	if len(codon) == 3:
		for 
		Peptide_Encoding(codon, Peptide)
		
		print 'tutto ok'
		
	iter += 3
	k_mers += 3	
'''

print '\nThe number of Nucleotides is ', ciclo+1
print 'The DNA_seq is composed by a length of ',len(DNA_seq),' nucleotides \n'
# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'
print 'End'
