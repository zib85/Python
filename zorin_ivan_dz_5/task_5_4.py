src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [j for i, j in zip(src, src[1:]) if j > i]
print(result)
