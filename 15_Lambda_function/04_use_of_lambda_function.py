# The power of lambda is better shown when you use them as an anonymous function inside another function.
#Use lambda functions when an anonymous function is required for a short period of time.
def myfun(n):
    return lambda x:x*n

lamb_func=myfun(2)#here myfun(2) returns the expression lambda x:x*2 which is lambda function to the lamb_func.now stil value of x is undefined so pass the value of x using lamb_func
print(lamb_func(4)) # lambda x:x*2 .in x the 4 comes and the expression is evaluated and return value