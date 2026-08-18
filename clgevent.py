# 14 08 2026

registrations = [
    ("S101", "Abhi", "Coding"),
    ("S102", "Rahul", "Hackathon"),
    ("S103", "Priyansh", "Coding"),
    ("S101", "Abhi", "Hackathon"),
    ("S104", "Sneha", "Robotics"),
    ("S105", "Amit", "Coding"),
    ("S106", "Neha", "Hackathon"),
    ("S103", "Priya", "Hackathon"),
    ("S107", "Rohit", "Robotics")
]


# 1. Display all registration records
print("-----All registration records-----")

for registartion in registrations:
    student_id, student_name, event_name = registartion

    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Event Name:",event_name)
    print("----------------------------------")


# 2. Create a list containing all student names

student_names = []

for registartion in registrations:
    student_id, student_name, event_name = registartion

    student_names.append(student_name)

print("\n-----Student Names-----")
print(student_names)


# 3. Convert student names list into a set
unique_students = set(student_names)

print("\n----- UNIQUE STUDENTS -----")
print(unique_students)
print("Total Unique Students:", len(unique_students))


# 4. Create a set containing all unique event names
event_names = []

for registration in registrations:
    student_id, student_name, event_name = registration

    event_names.append(event_name)

unique_events = set(event_names)

print("\n----- UNIQUE EVENTS -----")
print(unique_events)
print("Total Number of Events:", len(unique_events))

# 5. Create coding_students set
coding_students = set()

for registration in registrations:
    student_id, student_name, event_name = registration

    if event_name == "Coding":
        coding_students.add(student_name)

print("\n----- CODING STUDENTS -----")
print(coding_students)

# 6. Create hackathon_students set
hackathon_students = set()

for registration in registrations:
    student_id, student_name, event_name = registration

    if event_name == "Hackathon":
        hackathon_students.add(student_name)

print("\n----- HACKATHON STUDENTS -----")
print(hackathon_students)

# 7. Students participating in BOTH Coding and Hackathon
both_students = coding_students.intersection(hackathon_students)

print("\n----- STUDENTS IN BOTH CODING AND HACKATHON -----")
print(both_students)

# 8. Students participating ONLY in Coding
only_coding_students = coding_students.difference(hackathon_students)

print("\n----- STUDENTS ONLY IN CODING -----")
print(only_coding_students)

# 9. Add a new registration
print("\n----- ADD NEW REGISTRATION -----")

new_student_id = input("Enter Student ID: ")
new_student_name = input("Enter Student Name: ")
new_event_name = input("Enter Event Name: ")

# Create tuple
new_registration = (
    new_student_id,
    new_student_name,
    new_event_name
)

# Add tuple to registrations list
registrations.append(new_registration)

print("Registration added successfully.")

# 10. Search for a student and display all registered events
search_student = input("\nEnter student name to search: ")

found = False

print("\n----- STUDENT EVENTS -----")

for registration in registrations:
    student_id, student_name, event_name = registration

    if student_name.lower() == search_student.lower():
        print(student_name, "is registered for:", event_name)
        found = True

if found == False:
    print("Student not found.")


# ------------------------------------------------
# CHALLENGE TASK 1
# Find students registered for ONLY ONE event
# ------------------------------------------------

print("\n----- STUDENTS REGISTERED FOR ONLY ONE EVENT -----")

student_event_count = []

# Get unique students
unique_students = set(student_names)

# Add the newly registered student as well
for registration in registrations:
    student_id, student_name, event_name = registration
    unique_students.add(student_name)


for student in unique_students:

    student_events = set()

    for registration in registrations:
        student_id, student_name, event_name = registration

        if student_name == student:
            student_events.add(event_name)

    if len(student_events) == 1:
        student_event_count.append(student)


print(student_event_count)

# ------------------------------------------------
# CHALLENGE TASK 2
# Find the most popular event without dictionary
# ------------------------------------------------

print("\n----- MOST POPULAR EVENT -----")

# Create a set of unique events
unique_events = set(event_names)

# Add newly registered event
for registration in registrations:
    student_id, student_name, event_name = registration
    unique_events.add(event_name)

most_popular_event = ""
highest_count = 0

for event in unique_events:

    count = event_names.count(event)
    # Count newly added registrations also
    for registration in registrations:
        student_id, student_name, event_name = registration

        if event_name == event:
            if registration not in registrations[:9]:
                count += 1

    if count > highest_count:
        highest_count = count
        most_popular_event = event


print("Most Popular Event:", most_popular_event)
print("Number of Registrations:", highest_count)