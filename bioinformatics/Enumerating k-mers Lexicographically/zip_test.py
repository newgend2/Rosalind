# c = zip([1,2,3], [4,5,6])
# d = zip(['a','b','c'], ['d','e','f'])


# x = zip(c,d)
# for k,z in x:
#     print(k,z)

# print([['a','b','c']] * 3)
# print(len('abcd'))

def flatten(list_of_lists):
    """flatten lol"""
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


print(flatten([[1,2,3],[4,5,6]]))

print([1,2,3][:1])
print([3][1:])
print([1] + [2] + [3] + [] + [4] + [5] + [6] + [])