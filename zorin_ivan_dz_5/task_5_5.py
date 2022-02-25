src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_src = {}
for j in src:
    if j in new_src:
        new_src[j] += 1
    else:
        new_src[j] = 1
result = [el for el in src if new_src[el] == 1]
print(result)
