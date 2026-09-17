# 27 08 2026

file = open ("C:/Users/abhijit/Documents/SPRK Python Codes/data.txt", "x")
file.write ("Hello Students\n")
file.write ("Welcome to Python\n")
file.write ("We are doing advanced Python\n")
file.write ("Practicing file handling\n")
file.writelines ("Hello Students\nWelcome to Python\nWe are doing advanced Python\nPracticing file handling\n")
file.close()

file = open ("C:/Users/abhijit/Documents/SPRK Python Codes/data.txt", "r")
# content = file.read()

# print (content)
content = file.readlines()
print(content)
# content = file.readline()
# print (content)
file.close()
