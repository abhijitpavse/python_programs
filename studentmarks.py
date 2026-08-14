# 12 08 2026
# student marks management system

# step 1:empty list to store student marks

marks=[]    

# # Step 2: Accept marks of 10 students
print("Enter marks of 10 students:")

for i in range(10):
    mark = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

print("\nStudent Marks:", marks)

# 1. Display all student marks
print("\n1. All Student Marks:")
for mark in marks:
    print(mark)

# 2. Find the highest mark
print("\n2. Highest Mark:", max(marks))

# 3. Find the lowest mark
print("3. Lowest Mark:", min(marks))

# 4. Calculate the average mark
average = sum(marks) / len(marks)
print("4. Average Mark:", average)

# 5. Count students who passed
passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1

print("5. Students Passed:", passed)

# 6. Count students who failed
failed = 0

for mark in marks:
    if mark < 40:
        failed += 1

print("6. Students Failed:", failed)

# 7. Display marks above 75
print("7. Marks Above 75:")

for mark in marks:
    if mark > 75:
        print(mark)

# 8. Add marks for one new student using append()
new_mark = int(input("\n8. Enter marks of a new student: "))
marks.append(new_mark)

print("Updated Marks:", marks)

# 9. Remove the lowest mark using remove()
lowest = min(marks)
marks.remove(lowest)

print("\n9. After removing lowest mark:", marks)

# 10. Sort marks in ascending order
marks.sort()

print("\n10. Marks in Ascending Order:", marks)

# 11. Sort marks in descending order
marks.sort(reverse=True)

print("11. Marks in Descending Order:", marks)

# 12. Search for a particular mark
search_mark = int(input("\n12. Enter a mark to search: "))

if search_mark in marks:
    print("Mark found in the list.")
else:
    print("Mark not found in the list.")

# 13. Count how many students scored the searched mark
count = marks.count(search_mark)

print("13. Number of students who scored", search_mark, ":", count)


# Challenge Extension
# Update marks of a particular student

print("\n--- Challenge Extension ---")

position = int(input("Enter student position to update (1-11): "))
new_marks = int(input("Enter new marks: "))

marks[position - 1] = new_marks

print("Marks after updating:", marks)