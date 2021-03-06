
# imports

# structures
# import imp


DNA_complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
Nucleotides = ['A', 'C', 'T', 'G']


def fasta_read(file):
    """
    :param file: FASTA FILE
    :return: DICTIONARY WITH SEQUENCE TAGS AS KEYS AND SEQUENCES AS VALUES
    """
    with open(file) as f:
        file_raw = f.read().split()
        ros = [line for line in file_raw if '>' in line]
        file_edit = []
        for index, seq in enumerate(file_raw):
            if '>' in seq:
                file_edit.append('b')
            else:
                file_edit.append(seq)
        file_edit = ''.join(file_edit).split('b')[1:]
        file_edit = dict(zip(ros, file_edit))
        return file_edit


def amino_combo_dict():
    ''' 
    no inputs
    returns a dictionary of amino acid letter abrevs and the # of possible ways to get each letter from RNA

    '''
    import re
    from collections import Counter

    # reading codons
    with open('Inferring\ mRNA\ from\ Protein/codon_talbe.txt', 'r') as f_codon:
        aminos_counter = Counter(
            ''.join(re.findall(' [A-Z] | [A-Z]\\n', f_codon.read())).split())
        aminos_combos_dict = dict(
            zip(aminos_counter.keys(), aminos_counter.values()))

    return aminos_combos_dict


def countNucFrequency(seq):
    import collections

    '''Creates dictionary with # of nucleotides in sequence'''
    return dict(collections.Counter(seq))


def transcription(seq):
    '''Replaces T with U'''
    return seq.replace('T', 'U')


def reverse_complementDNA(seq):
    '''Swapping adenine with thymine and guanine with cytosine, then reversing'''
    return "".join(DNA_complement[nuc] for nuc in seq)[::-1]
