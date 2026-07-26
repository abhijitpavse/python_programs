### 20 07 2026
# WAC to print the name , select course and mode of payment from the user and print the receipt


name = input("Enter your name: ")
course = input("Enter your course: ")

p_mode = input("Enter your mode of payment (full / installments): ")
fees = int(input("Enter your fees: "))

# print("------Receipt-------")
# print("Welcome", name, "to", course, "course")
# print("Your mode of payment is:", p_mode, "and your fees is:", fees)
# print(course, "fees is:", fees)
# print("Total fees is:", fees)

print("\n---------------Receipt----------------\n")
print("Name: ", name,end="             ")
print("Course: ", course)
print("Mode: ", p_mode,end="              ")
print("Fees:   ", fees)
print("---------------------------------------")
print(course, end="                           ")
print(fees)

print("\n--------------------------------------")
print("Total fees: ", fees,sep="                     ")
print("\n---------------Thank You---------------\n")

