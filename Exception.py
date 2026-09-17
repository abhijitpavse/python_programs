# 26 08 2026
# from today we are learning about exception handling

# try:
#     num = int (input("Enter a number: "))
#     result = 10 / num
#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except ValueError:
#     print("Invalid input. Please try with numeric values.")

# except :
#     print("something went wrong try again")

# else:
#     print("division was successful")

# finally: # this statement will always run whether your program result successful or not
#     print("program exited")






# create a list for loop for i in range 0 to 3 try with index 4

# nums = [1,2,3,4]
# for i in range(0,5):
#     try:
#         print(nums[i])
#     except IndexError:
#         print("Index out of range")

# try:
#     number = [1,2,3,4]
#     a = int(input("Enter a number of element to be print:"))
#     for i in range(0,a):
#         print(number[i])

#     print()
# except IndexError:
#     print(f"there are only {len(number)} elements in the list")
# except ValueError:
#     print("Please try with numeric values")

# else:
#     print("Printing was successful")

# finally:
#     print("Program exited")



# write a program to check the age and raise a issue

# try:
#     age = int(input("Enter your age: "))

#     if age < 18:
#         raise ValueError("Age must be 18 or above.")

#     name = input("Enter your name: ")
#     print(name, "is eligible") 

# except ValueError as e:
#     print(e)



# salary 
try:
    sal = int(input("Salary:"))

    if sal<0:
        raise ValueError("Salary cannot be negative")

except ValueError as v:
    print(v)