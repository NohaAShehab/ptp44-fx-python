


# def sumnum(num1, num2):
#     res  = num1 + num2
#     print(res)
#     return res
#
#
#
# sumnum(4,5)
# sumnum('iti', 'fx')
# sumnum('iti', 34)

""" isdigit() ---> not correct """


# def sumnum(num1, num2):
#     if num1.isdigit() and num2.isdigit():
#         num1= int(num1)
#         num2 = int(num2)
#         res  = num1 + num2
#         print(res)
#         return res
#
#
#
# # sumnum(4,5)
# sumnum('iti', 'fx')
# sumnum(34, "iti")



""" never trust user input """



print(type(10))


x = type("noha")
print(x)
print(type(x))

l = [45,56,34,233]
print(type(l))

print(type(l)==list)


# def sumnum(num1, num2):
#     if type(num1)==int and type(num2)==int:
#         res = num1 + num2
#         return res
#
#     print('--- num1 and num2 should be integers ')
#
#
#
# l = []
# l.sort()



#
# """ isinstance """
#
#
# print(isinstance("iti", str))
#
#
# # def sumnum(num1, num2):
# #     if isinstance(num1, int) and isinstance(num2, int):
# #         res = num1+ num2
# #         print(res)
# #         return res
# #
# #     print("---- num1, num2 must be integers ")
# #
# #
# # sumnum(3,45)
# #
# # sumnum('2', 'rrr')
# # sumnum(4, 'iti')
#
# ###############################################
#
#

""" default arguments """
# def sumnums (num1=8, num2=9,num3=8):
#     print(f"num1 = {num1}, num2={num2}, num3={num3}")
#     res = num1 + num2 + num3
#     print(res)
#
# sumnums(3,5,6)
# sumnums(3,5)
# sumnums()





#
# print("tasnim", 'noha', 'iti', sep='+')
#
#
# print("I", end='#')
# print("love", end='#')
# print("iti")



#################################################
""" function accept any number of arguments """

print()

print(24,5)
print(4,56,3434,2,34)



# def askforstudents(*students):  # * represent zero or more
#     print(students, type(students))
#
#
# askforstudents()
# askforstudents('noha')
# askforstudents('ahmed', 'abdallah', 'wee', 'qewerwe')






def avg_numbers(*nums):
    summ= 0
    for n in nums:
        summ += n

    if nums:
        avg = summ/len(nums)
        print(avg)

avg_numbers(1,2,3, 423,4235,4)
avg_numbers(1,10,34,345,4)
avg_numbers()
















