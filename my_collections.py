# # 11 08 2026

#List 

# a = 10
# b = 20
# c = 30

# numbers=[10,20,30]
# alphabets=['d','y','u']
# fruits=["mango","apple","cherry"]

# print("a:",a)
# print("b:",b)

# print("Printing with Index Numbers")

# print(numbers[0])  # 0 is the index number of 10
# print(numbers[1])  # 1 is the index number of 20
# print(numbers[2])  # 2 is the index number of 30

# print(alphabets[0]) 
# print(alphabets[1])


# print(fruits[0])

# numbers.append(50)  # if want to add new numebr in existing list use append (it adds at last)
# print("after adding 50")

# print(numbers[3])
# print(numbers[-1]) #-1 is the index number of 50 used when we want to print last number(not known)

# # removing of numbers

# numbers.remove(30)
# print("after removing 30")
# print(numbers[0])
# print(numbers[1])
# print("at index 2 it is",numbers[2])

# # print(numbers[3]) there is no index 3

# numbers.insert(2,80) # inserting 80 at index 2

# print("updated index 2:",numbers[2])
# print("at index 3",numbers[3])

# print(len(numbers))

# print(numbers)

# print("Printing through for loop")
# for n in numbers:
#     if (n==numbers[-1]):   #this condition is for no quama at last 
#         print(n)
#     else:
#         print(n,end=", ")


# for n in fruits:  # printing same condintion for fruits and others
#     if (n==fruits[-1]):
#         print(n)
#     else:
#         print(n,end=", ")


# # tuple
# # in tuple we cannot change the value and we cannot add or remove

# student_data = (10,"Soham","Python",40000.00)
# print(student_data)

# for ele in student_data:
#     if (ele==student_data[-1]):
#         print(ele)
#     else:
#         print(ele,end=", ")

        

# # sets 
# # in sets stores only unique values using {} no sequence
# # in sets we cannot access the values using index

# student_id = {101,102,103,104,105,101}
# for id in student_id:
#     print(id)

# print("after adding 106")
# student_id.add(106)
# for id in student_id:
#     print(id)

# print("after removing 101")
# student_id.remove(101)
# for id in student_id:
#     print(id)

# print(student_id)


# 12 08 2026

# dictionary  (key value pair)
# in dictionary we can access the values using keys


# students_details = {
#     "id":101,
#     "name":'Abhijit',
#     "marks":80
# }
# print("Student name:",students_details["name"])

# #adding new details
# students_details["age"]=23

# print("Student age:",students_details["age"])

# for m,n in students_details.items():  # m & n are two variables which will store keys and values 
#     print(m,":",n)

# for multiple records

students_details = {
    "id":[101,102,103],
    "name":['Abhijit','Sarav','Arv'],
    "marks":[80,54,34]
}
students_details["name"][1]='Pavse'  # changing sarav to pavse

students_details["age"]=[23,24,21]

print("Student age:",students_details["age"])

for m,n in students_details.items():
    print(m,":",n[1]) # this will print sarav marks in 2nd index

for i in range(0,3):
    for m,n in students_details.items():
        print(m,":",n[i])



