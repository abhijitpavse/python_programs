# 20 08 2026

class Student:
    def __init__(self,roll_no,name,course,fees,phone,email):
        self.roll_no = roll_no # this is called field or
        self.name = name
        self.course = course
        self.fees = fees
        self.phone_no = phone
        self.emial_id = email

    def getBatch(self):
        if self.course == 'Data Analysis':
            return 'Python'
        elif self.course == 'Full-Stack':
            return 'MySQL'

s1 = Student(20,'Abhijit','Data Analysis',120000,'1236456436','abhi@gmail.com')
print(s1.name,"got",s1.getBatch(),"batch")

s2 = Student(21,'Pratik','Full-Stack',150000,'1236456432','pratik@gmail.com')
print(s2.name,"got",s2.getBatch(),"batch")


# inheritence , polymorphism, abstraction, encapsulation

# admin ka class and object


class Admin:

    def _init_(self):
        self.students = []

    # Add student
    def addStudent(self, student):

        self.students.append(student)

        print(student.name, "student added successfully")

    # Delete student
    def deleteStudent(self, roll_no):

        for student in self.students:

            if student.roll_no == roll_no:

                self.students.remove(student)

                print("Student deleted successfully")
                return

        print("Student not found")

# View students
    def viewStudents(self):

        for student in self.students:

            print(
                student.roll_no,
                student.name,
                student.course,
                student.fees,
                student.phone_no,
                student.email_id
            )

    # Update student
    def updateStudent(self, roll_no, name, course, fees, phone, email):

        for student in self.students:

            if student.roll_no == roll_no:

                student.name = name
                student.course = course
                student.fees = fees
                student.phone_no = phone
                student.email_id = email

                print("Student information updated successfully")
                return

        print("Student not found")
# Create Admin object

admin1 = Admin()


# Admin adds students

admin1.addStudent(s1)
admin1.addStudent(s2)


# View students

print("\nStudent List:")
admin1.viewStudents()


# Update student

print("\nUpdating Student:")
admin1.updateStudent(
    1,
    "Abhishek",
    "Full-Stack",
    850000,
    9999999999,
    "abhishek@gmail.com"
)


# View after update

print("\nStudent List After Update:")
admin1.viewStudents()


# Delete student
print("\nDeleting Student:")
admin1.deleteStudent(2)


# View after delete

print("\nStudent List After Delete:")
admin1.viewStudents()