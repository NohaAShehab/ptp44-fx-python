

""" use in operator """

#
# students = ['hend', 'nariman', 'basant','sara', 'asmaa', 'amany']
#
#
# print('asmaa' in students)
# print('reem' in students)


""" casting  string to a list """

#
# message= 'happy new year'
#
#
# message= list(message)
# print(message)
#
# message.reverse()
# print(message)
#
#
# ### convert list to string  ---> You must make sure that list consists only from strings
#
# data  =['python', 'houdini', 'maya', 'photoshop','conceptual art']
#
# newstring  = ' '.join(data)
# print(newstring)



""" generate list of 5 empty lists """


"""
    [[], [], [], [], []]

"""

myl= [[]]*5
print(myl)

# myl2= [10]
#
# myl2 = myl2*5
# print(myl2)
#


# myl2= ["iti", 'python']
#
# myl2 = myl2*5
# print(myl2)

""" convert string to list """

# message = "we          love python"
# message = message.split(" ")  # convert string to list based on delemiter
# print(message)  # remove ''
#
# num_of_empty_strings  = message.count('')
# print(num_of_empty_strings)
#
# while num_of_empty_strings > 0:
#     message.remove('')
#     num_of_empty_strings -=1
#
#
# print(message)
#
# new_message = ' '.join(message)
# print(new_message)
#

##
#
# message= 'we lovelove python'
# newmessage= message.split('love')
# print(newmessage)
#
