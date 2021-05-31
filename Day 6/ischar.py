ch = input()
if ch.isnumeric():
    print("The given input is number")
elif ch.isalpha():
    print("The given input is alphabet")
else:
    print("The given input is special characters")