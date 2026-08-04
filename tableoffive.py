# 28 07 2026 

# WAP to print the table of 5 

# -- using for loop

# for i in range(1, 11): # using range function
#     print("5 x", i, "=", 5 * i)


# num=5 # using variable  
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print (num*i)
# #print("loop over")


# num=5  # using variable in list this list is called as iterable list
# for i in list([1,2,3,4,5,6,7,8,9,10]):
#     print (num*i)

# for i in range(1, 11, 2): # using range function with step count
#      print("5 x", i, "=", 5 * i)

# for i in range(20, 41): 
#     print(i)

# print even numbers from 20 to 40
# for i in range(20, 41):
#     if i % 2 == 0:
#         print(i)
# print ("----")
# for i in range(20, 41):
#     if i % 2 != 0:
#         print(i)

#print even numbers on left and odd numbers on right side by side

for i in range(20, 41):
    if i % 2 == 0:
        print(i, end="        ")
    if i % 2 != 0:
        print(i)     


