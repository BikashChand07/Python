# __init__ function is like a constructor. constructor is used to initialize the object. All class have this __init__function which is always executed when the class is initiated or when the object is created.
#__init__ function has a parameter called self. The self parameter is the reference to the current instance of the class, and is used to access the variables that belongs to that class.

class student:
    def __init__(self, fullname,marks): #self paramater is mandatory to pass
        self.name=fullname
        self.marks=marks

s1=student("Bikash",67) # whenever the object is created the __inti__ function is executed or called.
print(s1.name,s1.marks)

s2=student("Ram",45)
print(s2.name,s2.marks)

'''
Default constructors:
def __init__(self): #self paramater is mandatory to pass
    print("default constructors")

parameterized constructors:

    def __init__(self, fullname,marks): #self paramater is mandatory to pass
        self.name=fullname
        self.marks=marks
'''