
def recur(alphabet, n):
    """return all strings in alphabet of length n ordered lexicographically"""
    if n == 1:
        return alphabet
    else:
        return [recur(alphabet, n - 1), ''.join([ltr * (len(alphabet)**(n -1)) for ltr in alphabet])]
        
def flatten(list_of_lists):
    """flatten lol"""
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

n = 4
alphabet = 'ABCDE'
strings = recur(alphabet, n) # get LoL of comination levels
flat_list = flatten(strings) # flatten LoL

print(strings)
print(flat_list)
# make every level repeat for the desired number of characters.
for i in range(len(flat_list) - 1):
    flat_list[i] *= int((len(alphabet)**n)/len(flat_list[i]))
# print(flat_list)
flat_list = flat_list[::-1] # reverse to print out in lexicographical order
# print out the strings in lexicograhic order
for z in range(len(flat_list[0])):
    print(''.join([flat_list[i][z] for i in range(len(flat_list))]))

