n=int(input())
for _ in range(n):
    string1=input()
    if len(string1)<=10:
        print(string1)
    else:
        print(f'{string1[0]}{len(string1)-2}{string1[-1]}')
