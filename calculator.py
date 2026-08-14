# write a program to calculate the calculator operation of a user input

# def calculator():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operator = input("Enter the operator (+, -, *, /): ")
#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         result = num1 / num2
#     else:
#         print("Invalid operator.")
#         return
#     print("Result:", result)

# calculator()


def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b    
def multiplication(a,b):
    return a * b    
def division(a,b):    
    return a / b

while True:
    print("Select operation choice:")
    print("1. Addition")                                    
    print("2. Subtraction")                                    
    print("3. Multiplication")
    print("4. Division")    
    print("5. Exit")

    choice = float(input("Enter choice(1/2/3/4/5): "))


    if choice == 5:
        print("Exit the calculator")
        break
    elif choice not in [1,2,3,4]:
        continue
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if choice == 1:
        print(a,"+",b,"=", addition(a,b))
    elif choice == 2:
        print(a,"-",b,"=", subtraction(a,b))
    elif choice == 3:
        print(a,"*",b,"=", multiplication(a,b))
    elif choice == 4:
        print(a,"/",b,"=", division(a,b))
   
    
    
 