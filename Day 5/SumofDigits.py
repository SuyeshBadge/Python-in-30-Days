'''
Given a number, find sum of its digits.

Examples :

Input : n = 687
Output : 21

Input : n = 12
Output : 3
'''

# n = input()
n=687
sum = 0
# for i in n:
#     sum += int(i)  # sum = sum + int(i)
# print(sum)

while n != 0:
    sum += int(n) % 10
    n=int(n)//10
print(sum)
