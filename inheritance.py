# Inheritance in Python program to print father and mother inheritance for Child  (multiple inheritance)

# 25 08 2026

class Father:
    
    def fathername(self):
        print("papa")
        # return "papa"

class Mother:
    # pass
    def mothername(self):
        print("mama")
        # return "mama"
    

class Child(Father,Mother):
    pass
    def childname(self):
        print("Abhi")
        # return "Abhi"

    # def __init__(self,name):
    #     Father.__init__(self,name)
    #     Mother.__init__(self,name)

c1=Child()
# print(c1.name) 

c1.fathername()
c1.mothername()
c1.childname()
