'''
Data type in python
int
float
string
list
tuple
dictionary
set
boolean (true or false)
'''
################################

'''
Iterable {list string tuples set dictionary}
non iterable {int float}
'''

#######################

# int float str
"""
int #integer for numbers 1,2,3,4
float #float for decimal numbers eg. 0.0 0.5
str #string for characters like "hello there"


"""


'''
integer stores all the numbers
non iterable
'''

a = 5
b = 10
print("a is "+str(a)+" and b is "+str(b))  # traditional method
print("a is {0} and b is {1}".format(a, b))  # string formatting
print(f'a is {a} and b is {b}')  # f string method

# a is 5 and b is 10


# float
"""
Float stores all the decimal points
non iterable
"""
f = 37.5
print(f)

# string
c = 'himanshu'
c1 = 'h'
print(c)

# list
'''
mutable
iterable
'''
list1 = [1, 2, 3, 4, 5, 6, 7]  # integer list
list2 = ['a', 'b', 'c']  # characters list
slist = [1, 1, 1, 1, 1.0, 1, 2, 1, 1]
# list1.pop()
print(list1[1])
print(slist)


# Tuples
'''
Tuples are immutable
iterable
'''
tup1 = (1, 2, 3, 4, 5)
# tup1[1]=5

# set
'''
address is not assinged to the block
only has distinct values
'''
s1 = {1, 2, 4, 3, 4, 100, 3, 4, 500, 4, 4}
s1list = set(slist)

# Dictionary
'''
dict_name={
    key:value,
    key:value,
    key:value,
    key:value

}
dict_name[key] => value
'''
himasnshu = [20, 'himanshu', 9384938493]  # list
print(himasnshu[2])
himanshu = {
    'Rollno': 20,
    'name': 'himanshu',
    'mobile': 9898938493
}  # dictionary
print(himanshu['mobile'])

# boolean
ismale = True
isfemale = False
