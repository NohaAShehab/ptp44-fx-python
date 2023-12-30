
"1- define a string "


# message = 'we love iti'

"2- get len of the string "

# print(len(message))
#
# """ 3- slice the string """
# s = message[5]
# print(s)
# print(message)



# newstring = message[5:]   #
# print(newstring)
# newstring = message[3:9]   #
# print(newstring)


# otherstring = message[::]
# print(otherstring)
#
# otherstring = message[::-1]
# print(otherstring)



# otherstring = message[::-2]
# print(otherstring)


"""3- count char in the string """
#
# print(message.count('i'))
# print(message.count('e'))
#
#
# students = 'ahmed and ahmed and ali and amira and salma and hager'
#
# print(students.count('Ahmed'))
#
#
""" concat 2 strings  """
# fname = 'Noha'
# midname= 'Abdelhady'
# lname='Shehab'
#
#
# # fullname= fname + midname + midname +  lname
# # print(fullname)
#
#
""" string interpolation"""
# fullname = fname + " "+ (midname + ' ')* 2 + lname
# print(fullname)


""" format string """

# no_of_students = 17
# course_name = 'houdini'

# message = 'we have ' + str(no_of_students) + " studies " + course_name
# print(message)

# # res = print(no_of_students)
# # print(res)
#
# print(print())


""" format the string using format function """
#
# no_of_students = 17
# course_name = 'houdini'
#
# temp_message = "we have {0} students study {1}."
# print(temp_message)
# new_message= temp_message.format(no_of_students, course_name)
# print(new_message)
#
# # new_message2 = temp_message.format(course_name, no_of_students)
# # print(new_message2)
# #
#
# temp_message = 'we have {abbasss} students study {hamada}'
# # new_message3 = temp_message.format(abbasss=no_of_students, hamada=course_name)
# new_message4 = temp_message.format(hamada = course_name, abbasss = no_of_students)
# print(new_message4)

"""f- format string """

name = 'ali'
track = 'fx'
# 1- create temp
# info = '{stdname} studies at {trackname}'
# 2- format temp
# newinfo = info.format(stdname=name, trackname= track)  # return with new string
# print(newinfo)
#
#
# # *create and format string at the same time based on existing varaibles
info = f'{name} studies at {track}'  # format string based on existing variables
# print(info)



""" string is immutable  datatype all 00> functions applied to the string ---> return new value """
# name = 'Ahmed'
# print(name)
#
# # newname = name.upper()
# #
# # print(newname, name)
# name = name.upper()    # assign new value
#
# print(name)
# print("--------")


""" upper lower , capitalize , title"""

msg = 'python is easy'

print(msg.upper())  # string.upper() ---> return new variable ===> value

print(msg.lower())

print(msg.capitalize())

print(msg.title())

""" ---------- examine content of the string -------"""
"""
    isdigit()
    isnumeric()
    isalpha()
    islower()
    isupper()
    istitle()
    iscapitalize()
    isspace()

"""
#
# message = input("please enter any input: ")
# print(f"message --isdigit {message.isdigit()}, -->isnumeric {message.isnumeric()}")
# print(f"message --isalpha {message.isalpha()}")
# print(f"message --islower {message.islower()}")
# print(f"message --isupper {message.isupper()}")
#
#
#
# str1 =''  # empty
# print(str1.isspace())
#
#
# str3 =' '
# print(str3.isspace())  # return True if string consists of only spaces
#
#
# str4= 'Madonna nasr'
# print(str4.isspace())


""" check if char exists in string  or not  (in operator )"""

# print('n' in "noha")

# newvar = 'iti'
# if 'iti' in newvar:
#     print(f"--- found ---> {newvar.count('iti')}")
# else:
#     print("--- not found =---")


#
# """ iterate over the string """
#
# message = 'weLoveITI'
#
# #
# # for abbass in message:  # [weloveITI]
# #     print(abbass)
# #
# #
# # print("-----")


