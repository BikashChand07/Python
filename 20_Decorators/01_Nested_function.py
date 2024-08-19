#assigning functions to the variabbles:
#we create a function that will add one to a number whenever it is called.We'll then assign the function to a varaible and use this variable to call the function
#def add_one(number):
#     number=number+1
#     return number


# plus_one=add_one
# print(plus_one(11))

#Nested Functions:Function inside another function
def plus_one(num):
    def add_one(num):
        num=num+1
        return num
    
    result=add_one(num)
    return result

print(plus_one(4))