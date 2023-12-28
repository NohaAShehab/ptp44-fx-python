
# variable name --->
## variable name must start with a-z or _
## variable mustn't contain special char
## variable can contain numbers
# variables in python are case sensitive
#
# name = 'Ahmed'
# Name = 'ali'
#
# # python is loosely dynamically typed lang.
# # 1- detect data type in the runtime
# # you can change the data type of variable in the runtime
#
# salary = input("please enter your salary: ")  # input function always saves the input into a string
# print(salary, type(salary))

# python support the variable name can refers to different datatype
# address = 10
#
# print(address, type(address))
# address ='cairo'
# print(address, type(address))


### python support type casting ((change datatype of variable))

""" convert string to int ---> """

# salary = input("please enter your salary: ")  # return with string
# print(salary, type(salary))

# change type of salary from string to int ?
# salary = int(salary)
# print(salary, type(salary))

# name = 'hend'
#
# "noha"


"""convert int to string """

# num = 17
# print(type(num), num)
# num = str(num)
# print(num, type(num))

""" convert bool to string  ---> True , False """

# mysalary = False
# print(type(mysalary), mysalary)
#
# mysalary = str(mysalary)
# print(mysalary, type(mysalary))
#
#
# happy = True
# happy = str(happy)
# print(happy, type(happy))


""" convert string to bool """

# name = 'noha'
#
# name=  bool(name)
# print(name, type(name))
#
#
# num = 10
# num = bool(num)
# print(num, type(num))
#
# numm = 'False'
# numm= bool(numm)
# print(numm, type(numm))
#
# num2= 0
# num2 = bool(num2)
# print(num2)
#
#
# name2= '      '
# # name2 = bool(name2)
# # print(name2)
#
#
# nmmm = '0'
# nmmm=  bool(nmmm)
# print(nmmm, type(nmmm))

""" string with triple qoutes --->"""
# single or double quoted string ignores the new lines in the string
bio = ('My name is Noha\n\n\n'
       'I works at ITI'
       'I lives in Cairo')

print(bio)

#triple quoted string --> keep track of new lines  --> represent it by \n
mybio = '''My name is Noha
I works at ITI
I lives in Cairo'''

print(mybio)


##############################################
# print(4+3)
#
# print(4-6)
# print(3**3)

#
# salary = 100
# salary *= 160  # salary = salary * 160
# print(salary)
#
# print(100 > 50)



######### And

"""
    and return True only if all the expression parts represents True ?
"""

print(True and True and 0 and 1)


"""
    or return True if only one of the expression parts represents True ?
"""

print(False or 0 or '' or True or 1)



""" not ? ---> """

print(not True )



