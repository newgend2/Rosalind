# read in fasta file

# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# ATCGGTA
# >Rosalind_3

# FASTA FILES CAN HAVE MULTIPLE LINES WHERE THE SEQUENCE IS IN BETWEEN SEPARATE SEQUENCES.
# The following algorithm extracts each sequence in its entirety even if it spans multiple lines.
file = 'rosalind_cons.txt'
with open(file) as f:
    # split file into list
    file_raw = f.read().split()
    seq = ""
    file_edit = []

    # get only sequences, combine sequences over multiple lines.
    for index, line in enumerate(file_raw):
        if '>' not in line and index != (len(file_raw) - 1):
            seq += line
        elif '>' in line and index != 0:
            file_edit.append(seq)
            seq = ''
        elif '>' in line and index == 0:
            seq = ''
        elif '>' not in line and index == (len(file_raw) - 1):
            seq += line
            file_edit.append(seq)

# print(file_edit)
# ________________________________________________

# build a profile matrix
# this involves counting how many of each letter there is in each spot for each dna string.

profile = {}
profile_consensus = []
# get all the first letters of each dna seq and so on...
for ltr in ['A', 'C', 'G', 'T']:
    intermed = []
    for seq_ltr in range(len(file_edit[0])):
        #
        ltr_column = ''.join([file_edit[seq_row][seq_ltr] for seq_row in range(0, len(file_edit))])
        # print(ltr_column)

        # for each letter build a row showing how many of that letter there is in each column position

        a = ltr_column.count(ltr)
        intermed.append(a)

    profile[ltr] = ''.join([str(str(z) + ' ') for z in intermed])
    profile_consensus.append(intermed)
# print(profile)
# print(profile.keys())
# print(profile_consensus)

# consensus
ltr_consensus = ['A', 'C', 'G', 'T']
consensus = []
for ltr_index in range(len(profile_consensus[0])):
    inter = [var[ltr_index] for var in profile_consensus]
    ltr_max = ltr_consensus[inter.index(max(inter))]
    consensus.append(ltr_max)

print(''.join(consensus))
# profile
for key in profile.keys():
    print(f'{key}:  {(profile[key])}')



