numlist_1 = [3, 9, 4, 2, 4, 1, 5, 6, 10, 8, 7, 9]
numlist_2 = [2, 2, 3, 2, 5, 6, 0, 8, 12 ]

set_1 = set(numlist_1)
set_2 = set(numlist_2)

method_1 = list(set_1 & set_2)
method_2 = list(set_1.intersection(set_2))

print("method_1: ", method_1)
print("method_2: ", method_2)