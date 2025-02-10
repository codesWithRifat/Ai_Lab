#Find the common elements between two lists using sets.

l1 = [9, 6, 3, 4, 5]
l2 = [3, 4, 5, 8, 7]

c = list(set(l1) & set(l2))
print(c)