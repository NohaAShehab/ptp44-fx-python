

# day = 'Thursday'  # assigment.
#
# # == comparison
# print( day =='Thursday')
# if day =='Thursday':
#     print("----let it go , the weekend is near ----")
# else:
#     print("---- it seems imposible until it is done -----")


#
# day = input("please enter day ")
# if day == "Sunday":
#     """ this block will be executed if the expression represent True """
#     print("----------------------------------------")
#     print("--- wish you good luck -----")
#     print("----------------------------------------")
# else:
#     print("------ Allah Maa3ak")




# name = ''
#
# if name:
#     print("hhii")
# else:
#     print("byeee")

""" check this """

# name = 'noha'
# if name:
#     print("---- hi ")
#
# print("---- Madoonnnnaa ----")


""" different cases needed to be checked """

#
# grade = 100
# if grade > 85:
#     print("---Excellent ---")
#
# if grade> 75:
#     print("----very good---")
#
# if grade >65:
#     print("----good ---")
#
# if grade > 60:
#     print("--- pass ")



"""

    if condition:
        do something 
    elif condition:
        do something
    elif condition:
        do something
    else:
        pass
"""



# grade = 66
# if grade >= 85:
#     print("---Excellent ---")
# elif grade>= 75:
#     print("----very good---")
# elif grade >=65:
#     print("----good ---")
# elif grade >=60:
#     print("--- pass ")
# else:
#     print("---Fail ---")



"""  ----> comparison operators works only between items from the same type """

# print("iti" > 100)


# grade = input("please enter your grade: ")  # always returns with string
# grade = int(grade)
# if grade >= 85:
#     print("--Excellent--")
# elif grade >= 75:
#     print("----very good---")
# elif grade >= 65:
#     print("----good ---")
# elif grade >= 60:
#     print("--- pass ")
# else:
#     print("---Fail ---")
#

""" isdigit() """

# grade = input("please enter your grade: ")  # always returns with string
# print(grade.isdigit())
# if grade.isdigit():
#     grade = int(grade)
#     if grade >= 85:
#         print("--Excellent--")
#     elif grade >= 75:
#         print("----very good---")
#     elif grade >= 65:
#         print("----good ---")
#     elif grade >= 60:
#         print("--- pass ")
#     else:
#         print("---Fail ---")
# else:
#     print("---- the input is not valid number ---- ")







salary = input("please enter your salary: ")  # this is a string
print(salary, type(salary))

""" I need to know what the string contains """

print(salary.isdigit())
## function used with string
# return True only if the string consists only from digits 0-9 other wise return false


if salary.isdigit():
    salary = int(salary)
else:
    print("--- please enter valid number ---")








