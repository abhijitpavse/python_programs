# 18 08 2026 

students = []

all_courses = set()

# --------------------------------------------------
# 1. Add Student
# --------------------------------------------------
def add_student():
    student_id = int(input("Enter Student ID:"))
    student_name = input("Enter Student Name:")

    # check if student already exist 
    for student in students:
        if student["info"][0] == student_id:
            print("Student ID already exist.")
            return

    # Tuple -> stores basic student information
    student_info = (student_id, student_name)


    # Dictionary -> stores all information of one student
    student = {
        "info" : student_info,
        "courses" : set(),
        "marks" : {}
    }

    students.append(student)

    print("Student added successfully.")

# --------------------------------------------------
# 2. Add Courses
# --------------------------------------------------

def add_courses():
    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["info"][0] == student_id:

            number = int(input("How many courses do you want to add? "))

            for i in range(number):
                course = input("Enter course name: ")

                # Set automatically prevents duplicates
                student["courses"].add(course)

                # Add course to overall course collection
                all_courses.add(course)

            print("Courses added successfully.")
            return

    print("Student not found.")


# --------------------------------------------------
# 3. Enter Marks
# --------------------------------------------------

def enter_marks():
    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["info"][0] == student_id:

            number = int(input("How many subjects do you want to enter marks for? "))

            for i in range(number):
                subject = input("Enter subject/course name: ")
                marks = float(input("Enter marks: "))

                student["marks"][subject] = marks

            print("Marks added successfully.")
            return

    print("Student not found.")


# --------------------------------------------------
# 4. Display Student Details
# --------------------------------------------------

def display_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["info"][0] == student_id:

            print("\n----- STUDENT DETAILS -----")

            print("Student ID:", student["info"][0])
            print("Student Name:", student["info"][1])

            print("Courses Enrolled:")

            if len(student["courses"]) == 0:
                print("No courses enrolled.")
            else:
                for course in student["courses"]:
                    print("-", course)

            print("Marks:")

            if len(student["marks"]) == 0:
                print("No marks entered.")
            else:
                for subject, marks in student["marks"].items():
                    print(subject, ":", marks)

            return

    print("Student not found.")


# --------------------------------------------------
# 5. Display All Students
# --------------------------------------------------

def display_all_students():

    if len(students) == 0:
        print("No students available.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:

        print("\nStudent ID:", student["info"][0])
        print("Student Name:", student["info"][1])

        print("Courses:", student["courses"])

        print("Marks:", student["marks"])

        print("--------------------------------")


# --------------------------------------------------
# 6. Display All Courses
# --------------------------------------------------

def display_all_courses():

    if len(all_courses) == 0:
        print("No courses available.")
        return

    print("\n----- ALL UNIQUE COURSES -----")

    for course in all_courses:
        print(course)

    print("Total Courses:", len(all_courses))


# --------------------------------------------------
# 7. Calculate Average Marks
# --------------------------------------------------

def calculate_average():

    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["info"][0] == student_id:

            marks = student["marks"]

            if len(marks) == 0:
                print("No marks available.")
                return

            total = sum(marks.values())
            average = total / len(marks)

            print("Student Name:", student["info"][1])
            print("Average Marks:", average)

            return

    print("Student not found.")


# --------------------------------------------------
# 8. Find Students Enrolled in a Course
# --------------------------------------------------

def find_students_by_course():

    search_course = input("Enter course name: ")

    found = False

    print("\nStudents enrolled in", search_course, ":")

    for student in students:

        if search_course in student["courses"]:
            print(student["info"][1])
            found = True

    if found == False:
        print("No students found for this course.")


# --------------------------------------------------
# 9. Remove a Course
# --------------------------------------------------

def remove_course():

    student_id = int(input("Enter Student ID: "))
    course = input("Enter course to remove: ")

    for student in students:

        if student["info"][0] == student_id:

            if course in student["courses"]:

                # Remove course from student's set
                student["courses"].remove(course)

                # Remove corresponding marks if present
                if course in student["marks"]:
                    del student["marks"][course]

                print("Course removed from student.")

                # Check whether any other student has this course
                course_still_used = False

                for other_student in students:

                    if course in other_student["courses"]:
                        course_still_used = True
                        break

                # Remove from overall course set only if nobody uses it
                if course_still_used == False:
                    all_courses.remove(course)
                    print("Course removed from overall course collection.")

                return

            else:
                print("Student is not enrolled in this course.")
                return

    print("Student not found.")


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

while True:

    print("\n======================================")
    print("   STUDENT COURSE MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Student")
    print("2. Add Courses")
    print("3. Enter Marks")
    print("4. Display Student Details")
    print("5. Display All Students")
    print("6. Display All Courses")
    print("7. Calculate Average Marks")
    print("8. Find Students Enrolled in a Course")
    print("9. Remove a Course")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        add_courses()

    elif choice == 3:
        enter_marks()

    elif choice == 4:
        display_student()

    elif choice == 5:
        display_all_students()

    elif choice == 6:
        display_all_courses()

    elif choice == 7:
        calculate_average()

    elif choice == 8:
        find_students_by_course()

    elif choice == 9:
        remove_course()

    elif choice == 10:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")