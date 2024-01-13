

""" tuple like a tuple ---> but immutable data type """



""" 1- to define a tuple """
#
t= tuple()
myt = ()


#
print(len(myt))
#
""" empty tuples are falsy values"""

if t:
    print("hii")
else:
    print("bye")
# #
print(bool(t))
#
#
""" tuple can hold different data from different data types """
#
mytuple= ("noha", 445, 'iti', True, 444.4555, None, ['python', 'houdini', 'maya', 'math',10])
#
print(mytuple)
print(len(mytuple))
#
#
""" access elements using index """
print(mytuple[3])
#
# print(mytuple[100])  # IndexError: tuple index out of range
print(mytuple[0][0])
#
# print(mytuple[6][1])
#
#
""" tuple is immutable   datatype """
# print(mytuple)
# mytuple[5]= 'updated'  #TypeError: 'tuple' object does not support item assignment


#
""" count element occurenece in the tuple """
print(mytuple.count("iti"))

# """get index of element in the tuple """
# index  --> return index of first occurence of element in the tuple
print(mytuple.index("noha"))
print(mytuple.index('iti'))

# #
#
#
item_index = 0
for item in mytuple:
    print(f"{item_index}-> {item}")
    item_index +=1
print("--------------")

#
"tuple concat"

grp1 = ('ahmed', 'mohamed', 'ali',33)
grp2 = ('python', 'houdini', 'maya', 'photoshop')
newtuple = grp1 + grp2  # newtuple
#
print(newtuple)
#

#################

#
students = ('hend', 'nariman', 'basant','sara', 'asmaa', 'amany')

#
print('asmaa' in students)
print('reem' in students)

#
# """ casting  string to a tuple """
#
# #
message= 'happy new year'


message= tuple(message)
print(message)


# #
# convert tuple to string  ---> You must make sure that tuple consists only from strings
# #
data  =('python', 'houdini', 'maya', 'photoshop','conceptual art')
#
newstring  = ' '.join(data)
print(newstring)
#
""" construct tuple of one item """
myt = ('noha',)
print(type(myt))
#
#
# """ generate tuple of 5 empty tuples """
#
#
# myt= ((),)*5
# print(myt)
#
