#class is like a blueprint for creating objects.To create class use keyword class.
class student:
    name="Ram"#attribute

    def __init__(self,name,marks): # constructor
        self.name=name
        self.marks=marks

    def hello(self):#method .remember always pass self parameter whether you use it or not
        print("hello student",self.name)

    def get_marks(self):
        return self.marks

#to create object/instance: syntax: objectname=classname()
s1=student("shyam",86)
# print(s1)
print(s1.name) #accessing the attribute
print(s1.hello())#accessing the method
print(s1.get_marks())


# s2=student()
# print(s2.name)