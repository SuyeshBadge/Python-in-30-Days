'''def iseven(n):
    if n % 2 == 0:
        return n


ar = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(map(iseven, ar))
for i in even:
    if i is not None:
        print(i, end=' ')'''
ar = [1, 2, 3, 4, 5, 6, 7, 8]
for i in ar:
    if i % 2 == 0:
        print(i, end=' ')
