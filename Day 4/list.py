"""
List : Array in python
syntax: a = [1,3,2,3]

one dimentional
simple = [1,2,3,4,1]

two dimentionsal
2d=[[1,2,3],
    [1,2,3],
    [1,2,3],
    ]


"""
a = [1, 2, 3]

# d=[[1,2],
#     [1,2],
#     [1,2],
#     ]

# BUILTIN FUNC
# len() => length of the list
# append() =>
a.append(4)
a.append(5)
a.append(6)
# insert() => it inserts an element at the given index
a.insert(10, 11)

ind = a.index(5)
# pop() => removes element at given index
# p=a.pop(0)
# removes() =>
# b=a.remove(6)

list1 = [22, 45, 12, 23, 12, 342, 4212, 100]
l = list1.sort(reverse=True)
list2 = sorted(list1, reverse=True)
l2 = list1.reverse()
l3 = list2.clear()

list2 = list1.copy()

list2.append(5)
print(list1)

c = list1.count(22)


harshal = ['h', 'a', 's']
himanshu = ['h', 'i', 'm']
m = himanshu.extend(harshal)



