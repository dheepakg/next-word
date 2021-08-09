a = {
    "": ["i", "i", "outside", "in", "flavored", "i"],
    "write": ["sql"],
    "like": ["cough"],
    "terms": ["of"],
    "python": ["for"],
    "food": ["and"],
    "dheepak": [],
    "fun": [],
    "self-taught": ["developer"],
    "blackcurrant": [""],
    "for": ["food"],
    "i": ["am", "am", "write", "am", "love", "tweet"],
    "bloke": [],
    "cough": ["syrup"],
    "been": ["programming"],
    "2014": [],
    "dosa,": ["and"],
    "tastes": ["like"],
    "syrup": [],
    "food,": ["i"],
    "ice": ["cream"],
    "love": ["dosa,"],
    "of": ["work,", "food,"],
    "a": ["self-taught", "confused", "lot"],
    "am": ["dheepak", "a", "a"],
    "yea,": ["it"],
    "tweet": ["a"],
    "confused": ["bloke"],
    "sql": ["for"],
    "cream": [],
    "since": ["2014"],
    "work,": ["i"],
    "and": ["i", "python", "blackcurrant"],
    "it": ["tastes"],
    "have": ["been"],
    "lot": [""],
    "developer": ["and"],
    "programming": ["since"],
    "in": ["terms"],
    "flavored": ["ice"],
    "outside": ["of"],
}

from collections import Counter


def count_elem_occurence_in_list(list_containing_elements):
    return Counter(list_containing_elements)


some_dict = {}
for item in a:
    # print(item, a[item])
    if len(item):
        val = dict(count_elem_occurence_in_list(a[item]))
        some_dict[item] = val

print(some_dict)
