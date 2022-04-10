

import sys
sys.path.insert(1, 'c:\\Users\\nate\\PycharmProjects\\Rosalind/')
# print(sys.path)
# import os
# print(os.getcwd())
from rosalind import fasta_read


file = './Rosalind/bioinformatics/Overlap Graphs/rosalind_grph.txt'

# Goal: create a dictionary out of fasta file with new sequence tags as keys and their
# Corresponding sequences strings as values
# with open(file) as f:
#     # split file into list
#     file_raw = f.read().split()
#     seq = ""
#     file_edit = []
#
#     # get only sequences, combine sequences over multiple lines.
#     for index, line in enumerate(file_raw):
#         if '>' not in line and index != (len(file_raw) - 1):
#             seq += line
#         elif '>' in line and index != 0:
#             file_edit.append(seq)
#             seq = ''
#         elif '>' in line and index == 0:
#             seq = ''
#         elif '>' not in line and index == (len(file_raw) - 1):
#             seq += line
#             file_edit.append(seq)
#
# ros = [line[1:] for line in file_raw if '>' in line]
# ros_dict = dict(zip(ros, file_edit))
# print(ros_dict)
# A suffix is a substring of a given string that includes the final character in the total string.
# A prefix is a substring of a given string that includes the first character in the total string.

# Create a directed graph
# take an integer k as an input.
# (s,t) where a length k suffix of s matches a length k prefix of t.
# s cannot be the same string as t.

# output
# Rosalind_1 Rosalind_2


# for a string, find all substrings of length k that contain the suffix
# for every other string find all substrings of length k that contain their prefix.
# If any suffix substring matches a prefix substring from the other strings, create an adjacency list.
# Once a string has been analyzed against all other strings. Remove it from the list because it does not need to be checked again.


# seqs = list(ros_dict.values())
# ros = list(ros_dict.keys())
#
# # create dictionaries for all suffix substrings and prefix substrings of each sequence string
# suffix_dict = {}
# prefix_dict = {}
# for i, seq in enumerate(seqs):
#     suffix = seq[-1]
#     prefix = seq[0]
#     suffix_dict[ros[i]] = [seq[index - 1:index + 2] for index in range(1, len(seq) - 1) if
#                            suffix in seq[index - 1:index + 2]]
#     prefix_dict[ros[i]] = [seq[index - 1:index + 2] for index in range(1, len(seq) - 1) if
#                            prefix in seq[index - 1:index + 2]]
# print(f'{suffix_dict}\n{prefix_dict}')
# for k, v in suffix_dict.items():
#     for k2, v2 in prefix_dict.items():
#         if k != k2:
#             match = bool(len([part for part in v2 if part in v]))
#             if match:
#                 print(f'{k}\t{k2}')


ros_dict = fasta_read(file)
seqs = list(ros_dict.values())
ros = list(ros_dict.keys())
k = 3
# create dictionaries for all suffix substrings and prefix substrings of each sequence string
suffix_dict = {}
prefix_dict = {}
for i, seq in enumerate(seqs):
    suffix_dict[ros[i]] = [seq[-k:]]
    prefix_dict[ros[i]] = [seq[0:k]]
print(f'{suffix_dict}\n{prefix_dict}')
for k, v in suffix_dict.items():
    for k2, v2 in prefix_dict.items():
        if k != k2:
            match = (v == v2)
            if match:
                print(f'{k} {k2}')
