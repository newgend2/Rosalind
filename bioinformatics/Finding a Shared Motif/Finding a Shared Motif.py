from rosalind import fasta_read

# read in file and put data in dict
file = 'rosalind_lcsm.txt'
ros_dict = fasta_read(file)

# get list of sequences
seqs = list(ros_dict.values())
dict_set = {}


# function to get all substrings of a given sequence
def get_substrings(input_seq):
    """

    :param input_seq: A fasta sequence string
    :return: a set of all substrings from length 1 to the entire string
    """
    substrings = set()
    for i in range(len(input_seq)):  # i is substring length
        # j is index of sequence so that the range stops according to substring len
        for j in range(i, len(input_seq)):
            seq = input_seq[j - i:j + 1]
            substrings.add(seq)
    dict_set[input_seq] = substrings


# for each fasta sequence, add its substring set to a dictionary containing subset sets for all sequences
for seq_test in seqs:
    get_substrings(seq_test)

# get intersection set of all sets
c = list(dict_set.values())
intersect_set = c[0]
for sets in c:
    intersect_set = intersect_set & sets

# print(intersect_set)

# get longest string from intersect to get longest common substring
list_intersect = list(intersect_set)
longest_common_substring = max(list_intersect, key=len)
print(longest_common_substring)
