##Protein Translation Problem

#Translate an RNA string into an amino acid string.
#Given: An RNA string Pattern.
#Return: The translation of Pattern into an amino acid string Peptide.

#Sample Dataset
'''
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
'''
#Sample Output
'''
MAMAPRTEINSTRING
'''
##########################################################################################

import os, sys, time
import Bio.Seq
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# start timing
startTime = time.time()
print 'Start'

path = os.path.join('E:\\','gential','Documents','Archivio_Coursesera','Coursera_BioinformaticsAlgorithms(Part1)','Rosalind','Bioinformatics_TextbookTrack')
In_filename = 'rosalind_2a.txt'					#'rosalind_2a_1_dataset.txt'
fText_in = os.path.join(path,In_filename)
In_filetext = open(fText_in,'r')
lines=In_filetext.readlines()
In_filetext.close()
Out_filename = 'output.txt'					#'rosalind_2a_1_output.txt'
fText_out = os.path.join(path,Out_filename)
Out_filetext = open(fText_out,'w')

values = []
for line in lines:
	values += line.split()
DNA_seq = values[0]
#DNA_seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
print DNA_seq

DNA_lenght = len(DNA_seq)
#print DNA_lenght

messenger_rna = Seq(DNA_seq, IUPAC.unambiguous_rna)
#print messenger_rna
protein = messenger_rna.translate()
print protein
Out_filetext.write(str(protein))

Out_filetext.close()

# show elapsed time
endTime = time.time()
print 'Entire DNA_seq elapsed time: ', endTime - startTime, ' seconds'
print 'End'
