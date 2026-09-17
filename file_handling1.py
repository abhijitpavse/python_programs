# 27 08 2026

# read mode
print("-----Read Mode-----")
try:
    file = open("C:/Users/abhijit/Documents/SPRK Python Codes/data2.txt", "r") # r = read
    content = file.read()
    print("File Content:",content)
    file.close()

except FileNotFoundError:
    print("data2.txt file not found")


# write mode

print("-----Write Mode-----")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes/data2.txt", "w")  # creates or overwrites
file.write("Hello Students\n")
file.write("This is write mode\n")
file.close()
print("data writen using write mode.")


# append mode

print("-----Append Mode-----")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes/data2.txt", "a")  # appends add at the end
file.write("This line is appended\n")
file.close()
print("Data appended.")


# Exclusive mode

print("-----Exclusive Mode-----")
try:
    file = open("C:/Users/abhijit/Documents/SPRK Python Codes/data2.txt", "x")  # exclusive  or we can create new file also
    file.write("File created using exclusive mode")
    file.close()
    print("data2.txt created using exclusive mode")
except FileExistsError:
    print("data2.txt File already exists")


# text mode

print("-----Text Mode-----")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes/data2.txt", "rt") # same as read mode
print("Text mode read:", file.read())
file.close



# Binary Mode 'b'

print("-----Binary Mode-----")
file = open("C:/Users/abhijit/Documents/SPRK Python Codes/binaryfile.bin", "wb") # binary mode
file.write(b"Hello Students")
file.close()

# read binary file
file = open("C:/Users/abhijit/Documents/SPRK Python Codes/binaryfile.bin", "rt")
data = file.read()
print("Binary data:",data)
file.close()