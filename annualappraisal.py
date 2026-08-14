# Employee Annual Appraisal Program


emp_name = input("Enter Employee Name: ")
current_salary = float(input("Enter Current Salary: "))
experience = float(input("Enter Years of Experience: "))
rating = float(input("Enter Performance Rating (1-5): "))


increment_percent = 0
bonus = 0


if rating == 5:
    if experience < 5:
        increment_percent = 15
    else:
        increment_percent = 20

elif rating == 4:
    if experience < 5:
        increment_percent = 10
    else:
        increment_percent = 12

elif rating == 3:
    increment_percent = 5

elif rating == 1 or rating == 2:
    increment_percent = 0

else:
    print("Invalid Performance Rating!")
    


increment_amount = (current_salary * increment_percent) / 100


revised_salary = current_salary + increment_amount


if revised_salary > 100000:
    bonus = 10000


print("\n========== EMPLOYEE APPRAISAL REPORT ==========")
print("Employee Name      :", emp_name)
print("Current Salary     : ₹", current_salary)
print("Experience         :", experience, "Years")
print("Performance Rating :", rating)
print("Increment %        :", increment_percent, "%")
print("Increment Amount   : ₹", increment_amount)
print("Bonus Amount       : ₹", bonus)
print("Revised Salary     : ₹", revised_salary)
print("==============================================")