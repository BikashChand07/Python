#There are two types of attributes: 1) class attribute 2)instance attribute

class student:
    # name,age,address are called attribute or property
    # name="ram"
    # age=22
    # address="ktm"
    college="SNSC"

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    #The attribute whose values are different for every instance of that class is called instance attribute. In this class "name" attribute is instance attribute  beacuse for different student they have different names.similarly name,age,address are also instance attribute. such attribute values are defined by using __init__ function.
    # 
    # and Those attribute whose values are same for every instance of that class is called class attribute. In this class 'college' attribute is common for all students(instance) of that class(student).  such attribute values are defined outside __init__ function.
    