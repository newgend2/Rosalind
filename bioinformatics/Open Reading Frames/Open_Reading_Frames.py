import numpy as np

# reading in fasta
with open('rosalind/bioinformatics/Open Reading Frames/input.txt', 'r') as raw_fasta:
    seq = ''.join(raw_fasta.read().splitlines()[1:])

# getting codon dictionary with codons as keys and corresponding amino acids as values
with open('rosalind/bioinformatics/Open Reading Frames/dna_codon_table.txt', 'r') as f_codon:
    codon_table = f_codon.read().split()
    codon_dict = {codon_table[z]: codon_table[z+1] for z in range(0, len(codon_table), 2)}

# getting reverse complement
complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
reverse_complement = ''.join([complement_dict[nuc] for nuc in seq][::-1])

# get all 6 reading frames
rf_original = [seq[i:] for i in range(3)]
rf_reverse_complement = [reverse_complement[i:] for i in range(3)]
rf = rf_original + rf_reverse_complement

# putting all reading frames into a dict
rf_codons = {}
for ind, rf_indiv in enumerate(rf):
    rf_codons[ind + 1] = [rf_indiv[i:i + 3] for i in range(0,(len(rf_indiv) // 3) * 3, 3)]

# getting all start and stop codon positions for each reading frame
start_stop_dict = {}
for ind, codons in rf_codons.items():
    start_stop_dict[ind] = [np.array([index for index, codon in enumerate(codons) if codon == 'ATG']), np.array([index for index, codon in enumerate(codons) if codon in ('TGA', 'TAA', 'TAG')])]


# get dictionary with reading frame as key and all ORF's within a frame as values. (orfs_frame_dict)
orfs_frame_dict = {}
for frame_num, start_stop_dict_frame in start_stop_dict.items(): 
    # get all ORFs for all 6 reading frames.
    if (start_stop_dict_frame[0].size > 0) and (start_stop_dict_frame[1].size > 0): # check there are no empty inds in either start or stop inds.
        
        # get list of stop codon list minus each start codon 
        stop_minus_start = [start_stop_dict_frame[1] - start_stop_dict_frame[0][i] for i in range(len(start_stop_dict_frame[0]))]
                    
        # get lengths of logical arrays that tell how many differences for each start codon are positive(meaning they are possible)
        diff_lengths = np.array([len(np.zeros(len(stop_minus_start[0]))[stop_minus_start[i] > 0]) for i in range(len(stop_minus_start))])

        # get the inds of the start codons that are in a working ORF. (these inds correspond to the ones in rf_condons[x][:])
        possible_start_inds = start_stop_dict_frame[0][diff_lengths > 0]  
        if np.any(possible_start_inds): # check that there are possible start inds
        # get the inds of the start codons that are in a working ORF (these inds correspond to the ones in stop_minus_start[x])
            start_codon_inds = np.arange(len(diff_lengths))[diff_lengths > 0]
            possible_end_inds = [start_stop_dict_frame[1][stop_minus_start[i] > 0][0] for i in start_codon_inds]

            orfs_frame_dict[frame_num] = list(zip(possible_start_inds, possible_end_inds))

# print(start_stop_dict)
# print(orfs_frame_dict)

# get all codon strings
codon_strings = []
for k,v in orfs_frame_dict.items():
    # print(k,len(v))
    for i in range(len(v)):
        codon_strings.append(rf_codons[k][v[i][0]: v[i][1]])

# translate codon ORFS into amino acids sequences. put them in a set to avoid repeats.
proteins = set()
for codon_seq in codon_strings:
    proteins.add(''.join([codon_dict[codon] for codon in codon_seq]))

for protein in proteins:
    print(protein) 
