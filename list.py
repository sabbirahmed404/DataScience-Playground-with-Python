numlist = [3, 9, 4, 2, 4, 1, 5, 6, 10, 8, 7, 9]

res = []

for i in numlist:
    if i not in res:
        res.append(i)

print(res)


# print(sorted(list(set(numlist))))