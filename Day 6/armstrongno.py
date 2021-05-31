#  if a no is equal to the cube of its all the elements then the no is called as an armstrong no.
'''
num=1 5 3

1^3 + 5^3 + 3^3 = 153


'''

n = input()
ans = 0
for i in n:
    ans += int(i)**len(n)
if ans == int(n):
    print("The no is an armstrong no.")
else:
    print("The number is not an armstrong number")
