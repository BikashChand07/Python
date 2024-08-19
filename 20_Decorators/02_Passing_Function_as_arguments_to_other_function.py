#Functions can also be passed as parameters to other functions.

#Example 1:
def plus_one(number):
    return number+1

def function_call(function): # here function is the plus_one function
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))

#Example 2:
def welcome(name):
    return (f"Hello {name}, Welcome to the programming world")

def greeting(function):
    print("This is greeting function")
    full_name=input("Please enter your name: ")
    return function(full_name)

print(greeting(welcome))



#functions returning another functions:
def hello_function():
    def say_hii():
        return "Hi"
    return say_hii

# hello=hello_function()
# print(hello()