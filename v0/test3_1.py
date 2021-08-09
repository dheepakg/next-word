from collections import Counter


l = ["am", "am", "write", "am", "love", "tweet"]


def count_elem_occurence_in_list(list_containing_elements):
    return Counter(list_containing_elements)


a = count_elem_occurence_in_list(l)
print(type(dict(a)))
print(dict(a))
