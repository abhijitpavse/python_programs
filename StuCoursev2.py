# 19 08 2026


data = []

while True:

    print("\n==============================")
    print(" Student Course Management")
    print("==============================")
    print("1. Add Student")
    print("2. Add Courses")
    print("3. Enter Marks")
    print("4. Display Student Details")
    print("5. Display All Students")
    print("6. Display All Courses")
    print("7. Calculate Average Marks")
    print("8. Find Students Enrolled in a Course")
    print("9. Remove a Course")
    print("10. Update Student Data")
    print("11. Exit")


    # =========================================================
    # Main Menu Choice
    # =========================================================

    while True:

        try:

            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= 11:
                break

            else:
                print("Invalid choice. Please enter 1 to 11.")

        except ValueError:

            print(
                "Invalid input. Please enter a number from 1 to 11."
            )


    # =========================================================
    # 1. Add Student
    # =========================================================

    if choice == 1:

        while True:

            try:

                stu_id = int(
                    input("Enter the Student ID: ")
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        # Check duplicate Student ID

        id_exists = False

        for s in data:

            if stu_id == s["info"][0]:

                id_exists = True
                break


        if id_exists:

            print("\nStudent ID already exists.")

        else:

            while True:

                stu_name = input(
                    "Enter the Student Name: "
                ).strip()

                if stu_name == "":
                    print(
                        "Student name cannot be empty."
                    )
                elif stu_name.isdigit():
                    print(
                        "Student name cannot be an integer."
                    )
                else:
                    break


            stu_info = (stu_id, stu_name)

            student = {
                "info": stu_info,
                "courses": set(),
                "marks": {}
            }

            data.append(student)

            print("\nStudent data Added")
            print(student)


    # =========================================================
    # 2. Add Courses
    # =========================================================

    elif choice == 2:

        while True:

            try:

                stu_id = int(
                    input("\nEnter Student ID: ")
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        for student in data:

            if stu_id == student["info"][0]:

                # Ask how many courses

                while True:

                    try:

                        number_of_courses = int(
                            input(
                                "\nHow many courses do you want to add? "
                            )
                        )

                        if number_of_courses <= 0:

                            print(
                                "Please enter at least 1 course."
                            )

                        else:

                            break

                    except ValueError:

                        print(
                            "Invalid input. "
                            "Please enter a number."
                        )


                # Add courses one by one

                for i in range(number_of_courses):

                    while True:

                        course = input(
                            f"Enter Course {i + 1}: "
                        ).strip()


                        # Empty course

                        if course == "":

                            print(
                                "Course name cannot be empty. "
                                "Please enter again."
                            )

                            continue


                        # Course cannot be integer

                        if course.isdigit():

                            print(
                                "Course name cannot be an integer. "
                                "Please enter a course name."
                            )

                            continue


                        # Check duplicate course

                        existing_courses = {
                            c.lower()
                            for c in student["courses"]
                        }


                        if course.lower() in existing_courses:

                            print(
                                course,
                                "already exists. "
                                "Please enter another course."
                            )

                            continue


                        # Add course

                        student["courses"].add(course)

                        print(
                            course,
                            "added successfully."
                        )

                        break


                print(
                    "\nCourses:",
                    student["courses"]
                )

                break

        else:

            print("Student not found.")


    # =========================================================
    # 3. Enter Marks
    # =========================================================

    elif choice == 3:

        while True:

            try:

                stu_id = int(
                    input("\nEnter Student ID: ")
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        for student in data:

            if stu_id == student["info"][0]:

                if len(student["courses"]) == 0:

                    print(
                        "\nThis student has no courses."
                    )

                    break


                # Display courses

                print(
                    "\nAvailable Courses:",
                    student["courses"]
                )


                while True:

                    course = input(
                        "Enter Course Name: "
                    ).strip()


                    if course == "":
                        print(
                            "Course name cannot be empty."
                        )
                        continue


                    if course.isdigit():

                        print(
                            "Course name cannot be an integer."
                        )
                        continue


                    course_found = None

                    for c in student["courses"]:

                        if c.lower() == course.lower():

                            course_found = c
                            break


                    if course_found is None:

                        print(
                            "Course is not enrolled "
                            "by this student."
                        )

                    elif course_found in student["marks"]:

                        print(
                            "Marks already entered for",
                            course_found
                        )

                    else:

                        while True:

                            try:

                                marks = int(
                                    input(
                                        "Enter Marks (0-100): "
                                    )
                                )

                                if 0 <= marks <= 100:

                                    break

                                else:

                                    print(
                                        "Marks must be "
                                        "between 0 and 100."
                                    )

                            except ValueError:

                                print(
                                    "Invalid marks. "
                                    "Please enter a number."
                                )


                        student["marks"][course_found] = marks

                        print(
                            "\nMarks added successfully."
                        )

                        print(
                            "Marks:",
                            student["marks"]
                        )

                        break

                break

        else:

            print("Student not found.")


    # =========================================================
    # 4. Display Student Details
    # =========================================================

    elif choice == 4:

        while True:

            try:

                search_id = int(
                    input(
                        "\nEnter Student ID to display: "
                    )
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        for s in data:

            if search_id == s["info"][0]:

                print("\n--- Student Details ---")
                print(
                    "Student ID:",
                    s["info"][0]
                )
                print(
                    "Student Name:",
                    s["info"][1]
                )
                print(
                    "Courses:",
                    s["courses"]
                )
                print(
                    "Marks:",
                    s["marks"]
                )

                break

        else:

            print("Student not found.")


    # =========================================================
    # 5. Display All Students
    # =========================================================

    elif choice == 5:

        print("\n--- All Students ---")


        if len(data) == 0:

            print("No students available.")

        else:

            for s in data:

                print(
                    "Student ID:",
                    s["info"][0]
                )

                print(
                    "Student Name:",
                    s["info"][1]
                )

                print(
                    "Courses:",
                    s["courses"]
                )

                print(
                    "Marks:",
                    s["marks"]
                )

                print()


    # =========================================================
    # 6. Display All Courses
    # =========================================================

    elif choice == 6:

        all_courses = set()


        for s in data:

            all_courses.update(
                s["courses"]
            )


        print("\n--- All Courses ---")

        if len(all_courses) == 0:

            print("No courses available.")

        else:

            print(all_courses)


    # =========================================================
    # 7. Calculate Average Marks
    # =========================================================

    elif choice == 7:

        while True:

            try:

                search_id = int(
                    input(
                        "\nEnter Student ID "
                        "to calculate average: "
                    )
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        for s in data:

            if search_id == s["info"][0]:

                if len(s["marks"]) == 0:

                    print(
                        "No marks available "
                        "for this student."
                    )

                else:

                    total = sum(
                        s["marks"].values()
                    )

                    number_of_subjects = len(
                        s["marks"]
                    )

                    average = (
                        total / number_of_subjects
                    )

                    print(
                        "\nStudent Name:",
                        s["info"][1]
                    )

                    print(
                        "Average Marks:",
                        average
                    )

                break

        else:

            print("Student not found.")


    # =========================================================
    # 8. Find Students Enrolled in a Course
    # =========================================================

    elif choice == 8:

        while True:

            search_course = input(
                "\nEnter Course Name to search: "
            ).strip()


            if search_course == "":

                print(
                    "Course name cannot be empty."
                )

            elif search_course.isdigit():

                print(
                    "Course name cannot be an integer."
                )

            else:

                break


        print(
            "\nStudents enrolled in",
            search_course,
            ":"
        )


        found = False


        for s in data:

            for course in s["courses"]:

                if (
                    course.lower()
                    == search_course.lower()
                ):

                    print(
                        s["info"][1]
                    )

                    found = True
                    break


        if found == False:

            print("No student found.")


    # =========================================================
    # 9. Remove a Course
    # =========================================================

    elif choice == 9:

        while True:

            try:

                search_id = int(
                    input(
                        "\nEnter Student ID: "
                    )
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        for s in data:

            if search_id == s["info"][0]:

                print(
                    "\nCurrent Courses:",
                    s["courses"]
                )


                while True:

                    remove_course = input(
                        "Enter Course to Remove: "
                    ).strip()


                    if remove_course == "":

                        print(
                            "Course name cannot be empty."
                        )

                    elif remove_course.isdigit():

                        print(
                            "Course name cannot "
                            "be an integer."
                        )

                    else:

                        break


                course_found = None


                for course in s["courses"]:

                    if (
                        course.lower()
                        == remove_course.lower()
                    ):

                        course_found = course
                        break


                if course_found is None:

                    print(
                        "\nCourse not found."
                    )

                else:

                    s["courses"].remove(
                        course_found
                    )

                    s["marks"].pop(
                        course_found,
                        None
                    )


                    print(
                        "\nCourse removed successfully."
                    )

                    print(
                        "Courses after removing:",
                        s["courses"]
                    )


                break

        else:

            print("Student not found.")


    # =========================================================
    # 10. Update Student Data
    # =========================================================

    elif choice == 10:

        while True:

            try:

                update_id = int(
                    input(
                        "\nEnter Student ID to update: "
                    )
                )

                break

            except ValueError:

                print(
                    "Invalid Student ID. "
                    "Please enter a number."
                )


        student_found = None


        for s in data:

            if update_id == s["info"][0]:

                student_found = s
                break


        if student_found is None:

            print("\nStudent not found.")

        else:

            while True:

                print(
                    "\n=============================="
                )

                print(
                    " What do you want to update?"
                )

                print(
                    "=============================="
                )

                print("1. Student Name")
                print("2. Course")
                print("3. Marks")
                print("4. Back to Main Menu")


                while True:

                    try:

                        update_choice = int(
                            input(
                                "\nEnter your choice: "
                            )
                        )

                        if 1 <= update_choice <= 4:
                            break

                        else:

                            print(
                                "Invalid choice. "
                                "Please enter 1 to 4."
                            )

                    except ValueError:

                        print(
                            "Invalid input. "
                            "Please enter a number."
                        )


                # -----------------------------------------
                # Update Student Name
                # -----------------------------------------

                if update_choice == 1:

                    while True:

                        new_name = input(
                            "Enter the New Student Name: "
                        ).strip()


                        if new_name == "":

                            print(
                                "Student name "
                                "cannot be empty."
                            )

                        elif new_name.isdigit():

                            print(
                                "Student name cannot "
                                "be an integer."
                            )

                        else:

                            break


                    old_id = student_found["info"][0]

                    student_found["info"] = (
                        old_id,
                        new_name
                    )


                    print(
                        "\nStudent name updated successfully."
                    )


                # -----------------------------------------
                # Update Course
                # -----------------------------------------

                elif update_choice == 2:

                    if len(
                        student_found["courses"]
                    ) == 0:

                        print(
                            "\nNo courses available."
                        )

                    else:

                        print(
                            "\nCurrent Courses:",
                            student_found["courses"]
                        )


                        while True:

                            old_course = input(
                                "Enter Course to Update: "
                            ).strip()


                            if old_course == "":

                                print(
                                    "Course name "
                                    "cannot be empty."
                                )

                            elif old_course.isdigit():

                                print(
                                    "Course name cannot "
                                    "be an integer."
                                )

                            else:

                                break


                        course_found = None


                        for course in student_found["courses"]:

                            if (
                                course.lower()
                                == old_course.lower()
                            ):

                                course_found = course
                                break


                        if course_found is None:

                            print(
                                "\nCourse not found."
                            )

                        else:

                            while True:

                                new_course = input(
                                    "Enter the New Course Name: "
                                ).strip()


                                if new_course == "":

                                    print(
                                        "Course name "
                                        "cannot be empty."
                                    )

                                    continue


                                if new_course.isdigit():

                                    print(
                                        "Course name cannot "
                                        "be an integer."
                                    )

                                    continue


                                duplicate = False


                                for course in student_found[
                                    "courses"
                                ]:

                                    if (
                                        course.lower()
                                        == new_course.lower()
                                    ):

                                        duplicate = True
                                        break


                                if duplicate:

                                    print(
                                        "New course "
                                        "already exists."
                                    )

                                else:

                                    break


                            student_found[
                                "courses"
                            ].remove(course_found)


                            student_found[
                                "courses"
                            ].add(new_course)


                            # Update marks key
                            if (
                                course_found
                                in student_found["marks"]
                            ):

                                old_marks = student_found[
                                    "marks"
                                ][course_found]


                                del student_found[
                                    "marks"
                                ][course_found]


                                student_found[
                                    "marks"
                                ][new_course] = old_marks


                            print(
                                "\nCourse updated successfully."
                            )

                            print(
                                "Courses:",
                                student_found["courses"]
                            )


                # -----------------------------------------
                # Update Marks
                # -----------------------------------------

                elif update_choice == 3:

                    if len(
                        student_found["marks"]
                    ) == 0:

                        print(
                            "\nNo marks available."
                        )

                    else:

                        print(
                            "\nCurrent Marks:",
                            student_found["marks"]
                        )


                        while True:

                            course_name = input(
                                "Enter Course Name "
                                "to Update Marks: "
                            ).strip()


                            if course_name == "":

                                print(
                                    "Course name "
                                    "cannot be empty."
                                )

                            elif course_name.isdigit():

                                print(
                                    "Course name cannot "
                                    "be an integer."
                                )

                            else:

                                break


                        course_found = None


                        for course in student_found["marks"]:

                            if (
                                course.lower()
                                == course_name.lower()
                            ):

                                course_found = course
                                break


                        if course_found is None:

                            print(
                                "\nMarks for this "
                                "course not found."
                            )

                        else:

                            while True:

                                try:

                                    new_marks = int(
                                        input(
                                            "Enter New Marks: "
                                        )
                                    )


                                    if (
                                        0
                                        <= new_marks
                                        <= 100
                                    ):

                                        break

                                    else:

                                        print(
                                            "Marks must be "
                                            "between 0 and 100."
                                        )

                                except ValueError:

                                    print(
                                        "Invalid marks. "
                                        "Please enter a number."
                                    )


                            student_found[
                                "marks"
                            ][course_found] = new_marks


                            print(
                                "\nMarks updated successfully."
                            )

                            print(
                                "Updated Marks:",
                                student_found["marks"]
                            )


                # -----------------------------------------
                # Back to Main Menu
                # -----------------------------------------

                elif update_choice == 4:

                    print(
                        "\nReturning to Main Menu..."
                    )

                    break


    # =========================================================
    # 11. Exit
    # =========================================================

    elif choice == 11:

        print(
            "\nProgram completed."
        )

        break