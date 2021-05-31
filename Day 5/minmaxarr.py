'''
Maximum and minimum of an array using minimum number of comparisons

input: 1 2 3 4 5 6
outpu: 6


'''

arr = list(map(int, input().split(' ')))

# method 1
# print(min(arr), max(arr))

# method 2

arr.sort()

print(f'min:{arr[0]} and max:{arr[-1]}')


# method 3

min1 = arr[0]
max2 = arr[1]
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i
print(min1, max2)
