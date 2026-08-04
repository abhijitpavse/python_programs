# 27 07 2026

# Cinema Ticket Calculator

# Base ticket price
base_price = 12

# Get user input
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").strip().lower()

# Calculate ticket price
if age < 12:
    # Child ticket
    ticket_price = 6

elif age >= 65:
    # Senior ticket (50% discount)
    ticket_price = base_price * 0.5

    # Weekend surcharge
    if day == "saturday" or day == "sunday":
        ticket_price += 2

else:
    # Standard adult ticket
    ticket_price = base_price

    # Wednesday discount
    if day == "wednesday":
        ticket_price -= 3

    # Weekend surcharge
    if day == "saturday" or day == "sunday":
        ticket_price += 2

# Display the final ticket price
print("Ticket Price: $", ticket_price)