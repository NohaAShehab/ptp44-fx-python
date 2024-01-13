

# fruits = ['apple', 'banana', 'cherry', 'orange', 'strawberry', 'watermelon', 'mango']
#
# # #
# for item in fruits:
#
#     if item== 'orange':
#         break
#     print(f'item= {item}')
#
#
# print("--- after the loop")
#
#
#
#
#
# for item in fruits:
#
#     if item== 'orange':
#         continue   # skipp current iteration
#     print(f'item= {item}')
#
# print("--- after the loop")



"""


    write a program that repeatedly asks the user to enter a name till he enters done then stop
"""

#
# names = []
# while True:
#     name = input("please enter your name: ")
#     if name=='done':
#         break
#     names.append(name)
#
# print(names)



""" """


# for turn in range(3):
#     password = input(f"please enter password for {turn+1}:")
#     if password=='abc':
#         print("""logged in successfully""")
#         break
#
#
#     print("--- password is incorrect, try again")
#
# if turn == 2 and password !='abc':
#     print(""" account has been locked """)




""" for else"""



# for i in range(5):
#     if i==3:
#         break
#     print(f'i = {i}')
#
# else:
#     print('---- loop ended ------')




# for turn in range(3):
#     password = input("please enter your password: ")
#     if password == 'abc':
#         print("\n-----logged in successfully-----\n")
#         break
#
#     print("--- please try again -----")
#
# else:
#     print("--- unfortunately your account has been locked ------ ")
#
#




for i in range(10):
    if i == 9:
        continue
    print(f"---i = {i}")

else:
    print("------------------loop reached its end ===========")


























