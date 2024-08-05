#Lambda function is also known as anonymous function.
#point to be remembered: A Lambda function can take any number of arguments, but can only have one expession.
'''
syntax:
lambda arguments or inputs: expression
The expression is executed and the result is returned
'''
#exanple: Add 10 to argument a and return the result:
x=lambda a:a+10
print(x(5))

def square(n):
    return n**2

print(square(4))

#The above square function can be written in a single line of code using lambda function
sq=lambda n:n**2 # the part n**2 is the return part of above square method.this part evaluate the expression and returns result and here n after lambda is the argument or input. we can pass any number of inputs or arguments
print(sq(4))
