# 30 07 2026

# write a code to display same input from user and when enter exit stops code

while(True):
    userinput = input("Enter what you want:")
    print (userinput) 
    if (userinput.lower() == 'exit'):
        break


# skip when user say skip and continue to next

while(True):
    userinput = input("Enter what you want:")
    print (userinput) 
    if (userinput.lower() == 'exit'):
        break
    elif userinput == "skip":
        continue
    else:
        print(userinput)


