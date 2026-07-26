# 23 07 2026
# take a input from the user to no of units consumed
# 0-100 units - 5 per unit
# 101-300 units - 7 per unit
# 301 and above - 10 per unit
# if bill exceeds 2000 then add 5% surcharge

# units = float(input("Enter the number of units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 300:
#     bill = 100 * 5 + (units - 100) * 7
# else:
#     bill = 100 * 5 + 200 * 7 + (units - 300) * 10
# # show the total bill to the user before adding the surcharge
# print("The total bill is:", bill)

# # show the total bill to the user after adding the surcharge
# if bill > 2000:
#     bill += bill * 0.05
# print("The total bill after surcharge is:", bill)


units = float(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 5
elif units >100 and units <= 300:
    bill = units * 7
elif units > 300:
    bill = units * 10



print("The total bill is:", bill)
# you surcharge of 5% if the bill exceeds 2000
if bill > 2000:
    bill = bill + (bill * 0.05)
print("The total bill after surcharge is:", bill)
