n = int(input())
notprime = False
for i in range(2, n):
    if n % i == 0:
        print("the no is not a prime number ")
        notprime = True
        break
if notprime == False:
    print("The given input is prime")
