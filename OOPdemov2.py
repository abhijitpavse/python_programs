# # entity == student
# # role == class,councellor, admin
# # class = data like name ,hw



# class Student:

#     def __init__(self, r, name, course, fees, phone, email):  # __init__ function is called constructor

#         self.roll_no = r
#         self.name = name
#         self.course = course
#         self.fees = fees
#         self.phone_no = phone
#         self.email_id = email

#     def getBatch(self):

#         if self.course == 'Data Analysis':
#             return 'python'

#         elif self.course == 'Full-Stack':
#             return 'MySql'

#         else:
#             return 'Batch not available'


# s1 = Student(1, "Abhi", "Data Analysis", 798789, 2342349, 'abhi@gmail.com')

# print(s1.name,"got",s1.getBatch(),"batch")

# s2 = Student(2, "Pratik", "Full-Stack", 7988789, 23423949, 'pratik@gmail.com')

# print(s2.name,"got",s2.getBatch(),"batch")


# # inheritence , polymorphism, abstraction, encapsulation

# # admin ka class and object


# class Admin:

#     def __init__(self):
#         self.students = []

#     # Add student
#     def addStudent(self, student):

#         self.students.append(student)

#         print(student.name, "student added successfully")

#     # Delete student
#     def deleteStudent(self, roll_no):

#         for student in self.students:

#             if student.roll_no == roll_no:

#                 self.students.remove(student)

#                 print("Student deleted successfully")
#                 return

#         print("Student not found")

# # View students
#     def viewStudents(self):

#         for student in self.students:

#             print(
#                 student.roll_no,
#                 student.name,
#                 student.course,
#                 student.fees,
#                 student.phone_no,
#                 student.email_id
#             )

#     # Update student
#     def updateStudent(self, roll_no, name, course, fees, phone, email):

#         for student in self.students:

#             if student.roll_no == roll_no:

#                 student.name = name
#                 student.course = course
#                 student.fees = fees
#                 student.phone_no = phone
#                 student.email_id = email

#                 print("Student information updated successfully")
#                 return

#         print("Student not found")
# # Create Admin object

# admin1 = Admin()


# # Admin adds students

# admin1.addStudent(s1)
# admin1.addStudent(s2)


# # View students

# print("\nStudent List:")
# admin1.viewStudents()


# # Update student

# print("\nUpdating Student:")
# admin1.updateStudent(
#     1,
#     "Abhishek",
#     "Full-Stack",
#     850000,
#     9999999999,
#     "abhishek@gmail.com"
# )


# # View after update

# print("\nStudent List After Update:")
# admin1.viewStudents()


# # Delete student
# print("\nDeleting Student:")
# admin1.deleteStudent(2)


# # View after delete

# print("\nStudent List After Delete:")
# admin1.viewStudents()
# # entity == student
# # role == class,councellor, admin
# #class = data like name ,hw



# class Student:

#     def __init__(self, r, name, course, fees, phone, email):

#         self.roll_no = r
#         self.name = name
#         self.course = course
#         self.fees = fees
#         self.phone_no = phone
#         self.email_id = email

#     def getBatch(self):

#         if self.course == 'Data Analysis':
#             return 'python'

#         elif self.course == 'Full-Stack':
#             return 'MySql'

#         else:
#             return 'Batch not available'


# s1 = Student(1, "Abhi", "Data Analysis", 798789, 2342349, 'abhi@gmail.com')

# print(s1.name,"got",s1.getBatch(),"batch")

# s2 = Student(2, "Pratik", "Full-Stack", 7988789, 23423949, 'pratik@gmail.com')

# print(s2.name,"got",s2.getBatch(),"batch")


# # inheritence , polymorphism, abstraction, encapsulation

# # admin ka class and object


# class Admin:

#     def __init__(self):
#         self.students = []

#     # Add student
#     def addStudent(self, student):

#         self.students.append(student)

#         print(student.name, "student added successfully")

#     # Delete student
#     def deleteStudent(self, roll_no):

#         for student in self.students:

#             if student.roll_no == roll_no:

#                 self.students.remove(student)

#                 print("Student deleted successfully")
#                 return

#         print("Student not found")

# # View students
#     def viewStudents(self):

#         for student in self.students:

#             print(
#                 student.roll_no,
#                 student.name,
#                 student.course,
#                 student.fees,
#                 student.phone_no,
#                 student.email_id
#             )

#     # Update student
#     def updateStudent(self, roll_no, name, course, fees, phone, email):

#         for student in self.students:

#             if student.roll_no == roll_no:

#                 student.name = name
#                 student.course = course
#                 student.fees = fees
#                 student.phone_no = phone
#                 student.email_id = email

#                 print("Student information updated successfully")
#                 return

#         print("Student not found")
# # Create Admin object

# admin1 = Admin()


# # Admin adds students

# admin1.addStudent(s1)
# admin1.addStudent(s2)


# # View students

# print("\nStudent List:")
# admin1.viewStudents()


# # Update student

# print("\nUpdating Student:")
# admin1.updateStudent(
#     1,
#     "Abhishek",
#     "Full-Stack",
#     850000,
#     9999999999,
#     "abhishek@gmail.com"
# )


# # View after update

# print("\nStudent List After Update:")
# admin1.viewStudents()


# # Delete student
# print("\nDeleting Student:")
# admin1.deleteStudent(2)


# # View after delete

# print("\nStudent List After Delete:")
# admin1.viewStudents()


# 24 08 2026

# polymorphism


class Person: #parent class
    def __init__ (self,id,name,phone,email):
        self.id=id
        self.name=name
        self.phone_no=phone
        self.email_id=email

    def showBasicInfo(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Phone Number:",self.phone_no)
        print("Email ID:",self.email_id)


class Student(Person): #child class
    def __init__(self, id,name,course,fees,phone,email):
        super().__init__(id, name, phone, email)
        self.course=course
        self.fees=fees

    def getBatch(self):
        if self.course == 'Data Analysis':
            return 'python'

        elif self.course == 'Full-Stack':
            return 'MySql'

    def visited(self):
        print(self.name,"Visited")

s1=Student(20,'Abhijit','Data Analysis',120000,'1236456436','abhi@gmail.com')
print(s1.name,"got",s1.getBatch(),"batch")
s1.showBasicInfo()

s2=Student(21,'Pratik','Full-Stack',150000,'1236456432','pratik@gmail.com')
print(s2.name,"got",s2.getBatch(),"batch")
s2.showBasicInfo()

class Admin(Person): #child class
    def __init__(self, id, name, phone, email,salary):
        super().__init__(id, name, phone, email)
        self.salary=salary
        self.students=[]
        self.batches=[]
        self.faculties=[]

    def visited(self):
        print("Admin Visited")

    def addStudent(self, student):
        self.students.append(student)
        print(student.name, "Student added successfully")

    def deleteStudent(self,id):
        for student in self.students:
            if student.id==id:
                self.students.remove(student)
                print("Student deleted successfully")
                return
        print("Student not found")

    def viewStudent(self):
        for student in self.students:
            print(student.id,
                  student.name,
                  student.phone_no,
                  student.email_id
            )

    def updateStudent(self,id,name,course,fees,phone,email):
        for student in self.students:
            if student.id==id:
                student.name=name
                student.course=course
                student.fees=fees
                student.phone_no=phone
                student.email_id=email
                print("Student information updated successfully")
                return
        print("Student not found")

    def deleteStudent(self,id):
        for student in self.students:
            if student.id==id:
                self.students.remove(student)
                print("Student deleted successfully")
                return
        print("Student not found")

    # student list after delete
    def viewStudent(self):
        for student in self.students:
            print(student.id,
                  student.name,
                  student.phone_no,
                  student.email_id
            )

