# 30 07 2026

# write a code to take input from user: username and password to verify its correct


username = 'admin'
password = 'secure'
while(username != 'admin' or password != 'very@secure'):
    print("Enter your Credintials:")
    username = input("Enter your username:")
    password = input("Enter your password:")
print("Welcome user")

# another way to write code after sussessful input exit the code

while(True):
    print("Enter your Credintials:")
    username = input("Enter your username:")
    password = input("Enter your password:")
    if(username=='admin' and password=='very@secure'):
        print("welcome user")
        break