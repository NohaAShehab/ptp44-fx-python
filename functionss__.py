#
# course=  'python'
# print("Ahmed", course)


#
# """ define a function"""
# # def saygoodmorning ():
# #     print("Good morning")
# #     return
#
# def saygoodmorning ():
#     print("Good morning")
#
# # calling the function
# res=saygoodmorning()
# print(res)
#
# saygoodmorning()
#
# saygoodmorning()
#
# saygoodmorning()
#



# print("10".isdigit())

# # print(len())
# print()



""" write a function that prints hello from ghaza """
""" function accepts zero arguments """

# def helloGhaza():
#     print("Hello From Ghaza")
#
#
#
# fun_res=helloGhaza()
# print(fun_res)


# helloGhaza("noha")


# def helloGhaza():
#     print("Hello From Ghaza")
#     return
#
#
#
# fun_res=helloGhaza()
# print(fun_res)


#
# """ write a function that asks the user to enter his/her name and print greating message for him/her"""
#
#
# def greetuser():
#     name = input("please enter your name: ")
#     great_message =  f"Nice to meet you {name}"
#     print(great_message)
#
#
#
# greetuser()



""" write a function that asks the user to enter his/her name and print 
greating message for him/her and return with name """


# def greetuser():
#     name = input("please enter your name: ")
#     great_message =  f"Nice to meet you {name}"
#     print(great_message)
#     return name
#
#
#
# customer_name=greetuser()



" function return more than one value "
""" write a function that asks the user to enter his/her first name lastname then return with 
firstname , lastname, fullname """

# def get_full_name():
#     fname= input("please enter first name: ")
#     lanme = input("please enter last name: ")
#     full_name = f'{fname} {lanme}'
#     return fname, lanme, full_name  # tuple
#
#
# myname = get_full_name()
# print(myname)

# def get_full_name():
#     fname= input("please enter first name: ")
#     lanme = input("please enter last name: ")
#     full_name = f'{fname} {lanme}'
#     return fname, lanme, full_name  # tuple
#
#
# myname = get_full_name()
# print(myname[0])


""" function can accpet parameters """


# def sumnum(num1, num2):
#     res = num1 + num2
#     print(f"from inside the function res = {res}")
#     return res
#
#
# sum_res= sumnum(10,20)
#
# print(sumnum(4,5))
# print("------------")

""" write a function that accept four numbers and return total, min, max of them """



# def nums_operations(num1, num2, num3, num4):
#     total = num1 + num2 + num3 + num4
#     minnumber= min(num1, num2, num3, num4)
#     maxnumber= max(num1, num2, num3, num4)
#     return total,minnumber, maxnumber
#
#
# res = nums_operations(2,4345,46,124)
# print(res)



# def minnum(a,b):
#     if a < b:
#         return a
#     return b
#
#
# def maxnum(a,b):
#     if a > b:
#         return a
#
#     return b
#
# def operations(a,b,c,d):
#     # minumber = minnum(d, minnum(c, minnum(a,b)))
#     minnn = minnum(minnum(a,b), minnum(c,d))
#     a_bmin = minnum(a,b)
#     c_dmin = minnum(c,d)
#     minn_ =  minnum(a_bmin,c_dmin)


"write a function that accepts list of numbers and return with newlist --> numbers * 2"

""" [2,45,6], [4,90, 12] """
# def myfunction(listofnumbers):
#     newlist = []
#     for i in listofnumbers:
#         newval = i*2
#         newlist.append(newval)
#
#     return newlist
#
#
# res =  myfunction([45,45,3,5,46])
# print(res)
""" try to implement the previous logic with another implementation """


# def amira_approach(listofnumbers):
#     newlist= []
#     k = 0
#     for i in listofnumbers:
#         print(i)
#         newlist.append(i*2)
#
#     return newlist
#
# print(amira_approach([43,3,34,34,3]))






# def abdallah_approach(listofnumbers):
#     k = 0
#     for i in listofnumbers:
#         listofnumbers[k] *=2  # listofnumbers[k] = listofnumbers[k]*2
#         k +=1
#
#     print(listofnumbers)
#
#
# abdallah_approach([4,5,63,3,34])
# print('---------------------------')
#







# def fady_approach(listofnumbers):
#
#     for index in range(len(listofnumbers)):
#         print(index)
#         listofnumbers[index] = listofnumbers[index]*2
#
#     print(listofnumbers)
#
#
# fady_approach([4,5,63,3,34])
# print('---------------------------')



""" """

#
# def noha_approach(listofnumbers):
#     no_of_elments = len(listofnumbers)-1
#
#     while no_of_elments >= 0:
#         listofnumbers[no_of_elments]= listofnumbers[no_of_elments]*2
#         no_of_elments -=1
#
#
#     print(listofnumbers)


# noha_approach([3,34,36,3,4,4])




































