# 25 08 2026 home work

# Hybrid Inheritance Example
# Person -> Student
# Person -> Employee -> Admin
# Person -> Employee -> Faculty


class Person:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show_person(self):
        print("Name  :", self.name)
        print("Phone :", self.phone)
        print("Email :", self.email)


class Student(Person):

    def __init__(self, name, phone, email,
                 student_id, course, fees):

        Person.__init__(self, name, phone, email)

        self.student_id = student_id
        self.course = course
        self.fees = fees

    def show_student(self):
        self.show_person()

        print("Student ID :", self.student_id)
        print("Course     :", self.course)
        print("Fees       :", self.fees)


class Employee(Person):

    def __init__(self, name, phone, email,
                 employee_id, salary, bank_name,
                 account_number, ifsc_code):

        Person.__init__(self, name, phone, email)

        self.employee_id = employee_id
        self.salary = salary
        self.bank_name = bank_name
        self.account_number = account_number
        self.ifsc_code = ifsc_code

    def show_employee(self):
        self.show_person()

        print("Employee ID    :", self.employee_id)
        print("Salary         :", self.salary)
        print("Bank Name      :", self.bank_name)
        print("Account Number :", self.account_number)
        print("IFSC Code      :", self.ifsc_code)


class Admin(Employee):

    def __init__(self, name, phone, email,
                 employee_id, salary, bank_name,
                 account_number, ifsc_code,
                 list_batches, list_faculty, list_students):

        Employee.__init__(
            self,
            name, phone, email,
            employee_id, salary, bank_name,
            account_number, ifsc_code
        )

        self.list_batches = list_batches
        self.list_faculty = list_faculty
        self.list_students = list_students

    def show_admin(self):
        self.show_employee()

        print("Batches  :", self.list_batches)
        print("Faculty  :", self.list_faculty)
        print("Students :", self.list_students)


class Faculty(Employee):

    def __init__(self, name, phone, email,
                 employee_id, salary, bank_name,
                 account_number, ifsc_code,
                 batch_schedule, list_students):

        Employee.__init__(
            self,
            name, phone, email,
            employee_id, salary, bank_name,
            account_number, ifsc_code
        )

        self.batch_schedule = batch_schedule
        self.list_students = list_students

    def show_faculty(self):
        self.show_employee()

        print("Batch Schedule :", self.batch_schedule)
        print("Students       :", self.list_students)


# -------------------------------------------------
# Student Object
# -------------------------------------------------

s1 = Student(
    "Abhijit",
    "9876543210",
    "abhijit@gmail.com",
    101,
    "Data Science",
    50000
)

print("----- STUDENT DETAILS -----")
s1.show_student()


# -------------------------------------------------
# Admin Object
# -------------------------------------------------

a1 = Admin(
    "Rahul",
    "9876500000",
    "rahul@gmail.com",
    201,
    60000,
    "SBI",
    "1234567890",
    "SBIN0001234",
    ["Python", "SQL"],
    ["ABC Sir", "XYZ Sir"],
    ["Student1", "Student2"]
)

print("\n----- ADMIN DETAILS -----")
a1.show_admin()


# -------------------------------------------------
# Faculty Object
# -------------------------------------------------

f1 = Faculty(
    "ABC Sir",
    "9876511111",
    "abc@gmail.com",
    301,
    55000,
    "HDFC",
    "9876543210",
    "HDFC0001234",
    "10 AM - 12 PM",
    ["Student1", "Student2", "Student3"]
)

print("\n----- FACULTY DETAILS -----")
f1.show_faculty()