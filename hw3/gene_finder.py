# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Maor Bernstein
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents a protein coding region).
        
        dna: a DNA seq_aciuence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """

    l = 0
    out = ""
    for i in range(len(dna)/3):
        for j in range(len(codons)):
            for k in range(len(codons[j])):
                if dna[3*i:3*i+3]==codons[j][k]:
                    l = 5
                    break
            if l==5:
                out = out + aa[j]
                break
        l = 0;
    return out

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    x = "AAA"
    y = "CAGCGTTGGATGCAA"
    z = "ATAATGTGTAATCA"
    xeo = "K"
    yeo = "QRWMQ"
    zeo = "IMCN"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + coding_strand_to_AA(x)
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + coding_strand_to_AA(y)
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + coding_strand_to_AA(z)


def complement(letter):
   """ Computes the complement of a single DNA character
    
        letter: A single DNA character ('A','T','C','G')
        returns: the complement of the DNA character
    """
    
   if letter=="A":
        return "T"
   if letter=="C":
        return "G"
   if letter=="T":
        return "A"
   if letter=="G":
        return "C"
   return 

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    n = len(dna)
    rev = ""
    for i in range(n):
        rev = rev + complement(dna[n - 1 - i]) 
    return rev

def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    x = "AAA"
    y = "CAGCGTTGGATGCAA"
    z = "ATAATGTGTAATCA"
    xeo = "TTT"
    yeo = "TTGCATCCAACGCTG"
    zeo = "TGATTACACATTAT"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + get_reverse_complement(x)
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + get_reverse_complement(y)
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + get_reverse_complement(z)    
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    out = "ATG"
    for i  in range(3,len(dna),3):
        cod = dna[i:i+3]
        if (cod=="TAG") or (cod == "TAA") or (cod =="TGA"):
            break;
        out = out + cod
    return out

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    x = "ATG"
    y = "ATGTTTTGATGAA"
    z = "ATGATGTGTAGATCA"
    xeo = "ATG"
    yeo = "ATGTTT"
    zeo = "ATGATGTGTAGATCA"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + rest_of_ORF(x)
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + rest_of_ORF(y)
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + rest_of_ORF(z)    
       
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    orfs = []
    i=0
    while i<len(dna):
        if dna[i:i+3]=="ATG":
            ORF = rest_of_ORF(dna[i:])
            orfs.append(ORF)
            i = i + 3 + len(ORF)
        else:
            i = i + 3
    return orfs

     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    x = "ATGGGGGGGTGA"
    y = "ATGTTTTAAATGAAATAG"
    z = "ATGGGGTAGGGGATGCCCTAA"
    xeo = "[ATGGGGGGG]"
    yeo = "[ATGTTT,ATGAAA]"
    zeo = "[ATGGGG,ATGCCC]"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + str(find_all_ORFs_oneframe(x))
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + str(find_all_ORFs_oneframe(y))
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + str(find_all_ORFs_oneframe(z))

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    out = []
    for i in range(3):
        out.extend(find_all_ORFs_oneframe(dna[i:]))
    return out


def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    x = "ATGGATGGTGAATGAGTGA"
    y = "ATGTTTTAATGAAATAG"
    z = "ATGGGGTAGTGAGGTATGAGCTACCTATGAA"
    xeo = "[ATGGATGGTGA,ATGGTGAATGAG,ATGAGTGA]"
    yeo = "[ATGTTT,ATGAAA]"
    zeo = "[ATGGGG,ATGAGCTACCTA,ATGAA]"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + str(find_all_ORFs(x))
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + str(find_all_ORFs(y))
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + str(find_all_ORFs(z))  



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    out = []
    out.extend(find_all_ORFs(dna))
    out.extend(find_all_ORFs(get_reverse_complement(dna)))
    return out


def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    x = "ATGGATGGTGAATGAGTGA"
    y = "ATGTTTTAATGAAATAG"
    z = "ATGGGGTAGTGAGGTATGAGCTACCTATGAA"
    xeo = "[ATGGATGGTGA,ATGGTGAATGAG,ATGAGTGA]"
    yeo = "[ATGTTT, ATGAAA]"
    zeo = "[ATGGGG,ATGAGCTACCTA,ATGAA]"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + str(find_all_ORFs_both_strands(x))
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + str(find_all_ORFs_both_strands(y))
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + str(find_all_ORFs_both_strands(z))



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    t = find_all_ORFs_both_strands(dna)
    j = 0
    longest = t[0]
    for i in range(1,len(t)):
        if len(t[i]) > len(longest):
            longest = t[i]
    return longest


def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    x = "ATGGATGGTGAATGAGTGA"
    y = "ATGTTTTAATGAAATAG"
    z = "ATGGGGTAGTGAGGTATGAGCTACCTATGAA"
    xeo = "ATGGATGGTGAA"
    yeo = "ATGTTT"
    zeo = "ATGAGCTACCTA"
    print "input: " + x + ", expected output: " + xeo + ", actual output: " + longest_ORF(x)
    print "input: " + y + ", expected output: " + yeo + ", actual output: " + longest_ORF(y)
    print "input: " + z + ", expected output: " + zeo + ", actual output: " + longest_ORF(z)


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    import random
    out = 0
    t = list(dna)
    for i in range(num_trials):
        random.shuffle(t)
        dna_shuffled = collapse(t)
        if len(longest_ORF(dna_shuffled)) > out:
            out = len(longest_ORF(dna_shuffled))
    return out
        

def gene_finder(dna,threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    t = find_all_ORFs_both_strands(dna)
    orfs = []
    aas = []
    for i in t:
        if len(i) > threshold:
            orfs.append(i)
    for i in orfs:
        aas.append(coding_strand_to_AA(i))
    return aas


    

    
