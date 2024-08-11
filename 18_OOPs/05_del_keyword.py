#del keyword is used to delete object properties or object itself
class Student:
    def __init__(self,name):
            self.name=name

s1=Student("Bikash")
print(s1.name)
del s1 #delete object s1
print(s1.name) #NameError: name 's1' is not defined because s1 object as well as information related to s1 object is deleted. 

