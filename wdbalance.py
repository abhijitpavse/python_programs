# 21 07 2026
# WAP to print the initial balnce 10000 and ask user to withdraw the amount and print the remaining balance 

# balance= 10000
# print("Initial balance:", balance)

# withdraw = float(input("Enter the amount to withdraw: "))
# if withdraw <= balance:
#     balance -= withdraw
#     print("Withdrawal successful.", end=" ")
#     #print("Remaining balance:", balance)

# else:
#     print("Insufficient balance. You cannot withdraw that amount.")
# print("Remaining balance:", balance)    

#
#now give the user an option to deposit the amount and print the remaining balance after deposit 

balance= 10000
choice = input("Enter 1 to see the Initial Balance, 2 to Deposit the Amount and 3 to Withdraw the Amount: ")

if choice == "1":
    print("Initial balance:", balance)
elif choice == "2":  # take only positive values for deposit
    deposit = float(input("Enter the amount to deposit: "))
    if deposit > 0:
        balance += deposit
        print("Deposit successful.", end=" ")
        print("Remaining balance:", balance)
    else:
        print("Invalid deposit amount.")
elif choice == "3":
    withdraw = float(input("Enter the amount to withdraw: "))
    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful.", end=" ")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance. You cannot withdraw that amount.")
        print("Remaining balance:", balance)
else:
    print("Invalid choice.")
