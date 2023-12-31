

""" ---> replace ------"""

# msg = 'a  a  We support Ghaza a   a   a'  #replace---> a ===> @
#
# # newmessage = msg.replace('a', '@')  # return new string
# #
# # print(newmessage)
#
#
# newmessage = msg.replace('a', '@', 2)  # return new string
#
# print(newmessage)


#########
""" ---> NEVER TrusT User Input -------"""
""" check this scenario """

# name = input("please enter your name: ")
#
# print(name)
# print(len(name))
#
# name=  name.strip()
# print(name, len(name))



#
#
# message = input("------------ leave message ---------------")
# print(message)
# print(message.isspace())


# name = '                 noha          shehab                   '
# newname= name.strip() # remove spaces from the beginning and the end of the string
# print(newname)
#
# newname2= newname.replace(' '*(newname.count(' ')-1), '')
# print(newname2)


# newname = name.lstrip()
# print(newname)
#
# newname = name.rstrip()
# print(newname)



""" --- check this """

message= '   ------ wish you happy new year --------   '
# print(message)
# newmessage = message.strip('- r')  # accept set of chars to be stripped from the beginning and the end of the string
# print(newmessage)




""" check this """

# fullname = input("please enter name:  ")

# if fullname.isalpha() and not fullname.isspace() and not fullname.isdigit():
#     print("--- name ====")
# else:
#     print("---- error ")


# if fullname.isalpha():
#     print("--- name ====")
# else:
#     print("---- error ")



""" password --> 12 , numbers , chars """


# password = input("please enter password: ")
#
# if len(password)>12 and not password.isspace() and not password.isdigit() and not password.isalpha():
#     print("valid password", password)
# else:
#     print("--- invalid password ----")

















#
# emaill = input('Enter your email: ')
# if '.' in emaill and emaill.count('@')==1:
#     print("--- valid email")
#
#

""" min , max string """

min_str = min("Ahmed",'Salma', 'ahmed', 'abdallah','Nariman', 'Abdulrahman', 'noha', '444','55645')
print(min_str)







