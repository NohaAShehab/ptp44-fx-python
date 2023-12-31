

""" 1- to define a list """

l = []
print(type(l))
myl = list()
print(type(myl))

print(len(myl))

""" empty lists are falsy values"""

# if l:
#     print("hii")
# else:
#     print("bye")
#
# print(bool(l))


""" list can hold different data from different data types """

mylist= ["noha", 445, 'iti', True, 444.4555, None, ['python', 'houdini', 'maya', 'math',10]]

print(mylist)
print(len(mylist))


""" access elements using index """
print(mylist[3])

# print(mylist[100])  # IndexError: list index out of range
print(mylist[0][0])

print(mylist[6][1])


""" list is mutable is mutable  datatype """
print(mylist)
mylist[5]= 'updated'
print(mylist)

""" append new element to the list ===> add element at the end of the list"""
mylist.append('iti')
print(mylist)
""" insert element at certain position  in the list """
mylist.insert(4, 'iti')
print(mylist)


mylist.insert(100 , 'inserted value')
print(mylist)

mylist.insert(50 , 'sara')
print(mylist)
print('--------------------')

mylist.insert(-3, 'abc value')
print(mylist)

""" remove elements from list """
"1- pop ==> remove element from the end of the list"
popped_value =mylist.pop()  # return with popped value
print(mylist)

""" pop element from list at certain position / index """

popped_value = mylist.pop(5)
print("\n", popped_value)
print(mylist)

mylist.pop()


""" remove specific element from list """
mylist.remove('iti')  # remove first occurrence of element from the list

print('\n\n',mylist)

# """ count element occurenece in the list """
# print(mylist.count("iti"))
#
"""get index of element in the list """
# # index  --> return index of first occurence of element in the list
# print(mylist.index("noha"))
# print(mylist.index('iti'))
#
#

""" get index of each element in the list """

item_index = 0
for item in mylist:
    print(f"{item_index}-> {item}")
    item_index +=1
print("--------------")


"list concat"

grp1 = ['ahmed', 'mohamed', 'ali',33]
grp2 = ['python', 'houdini', 'maya', 'photoshop']
newlist = grp1 + grp2  # newlist

print(newlist)

""" extend a list """


content = ['intro', 'if condition', 'loops', 'datatypes']
print(content)
another_content =['list', 'tuple', 'set','break','continue']

content.extend(another_content)

print(content)


""" sort the list ---.> comparison --->  you can sort lists consists of elements from the same datatype"""
print("\n\n")
names = ['AbdAllah', 'Nariman', 'Hager', 'salma', 'Reem', 'Ahmed','abdulrahman', 'madonna', 'fady']
print("before sort", names)
names.sort()
print(names)

# res = names.sort()
# print(res)

# """ sorting descending """
# names.sort(reverse=True)
# print(names)


""" reverse  a list """
print('\n\n\n', mylist)
mylist.reverse()
print('\n\n\n', mylist)




