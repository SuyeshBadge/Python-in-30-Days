n=int(input())


def factorial(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact


for i in range(n+1):
    print(f'The factorial of {i} is {factorial(i)}')
'''

5
5x4x3x2x1

nCr= n!/(n-r)!xr!


'''