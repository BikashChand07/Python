'''
As we know that Function can call another function. It is also possible to call a function itself ,these types of functions are called recursive function. To be a Recursive Function two conditions must be satisifed :
1)function should call itself
2)base condition/ terminating condition
'''
#Example1: find factorial of number using recursion
def factorial(n):
    if(n<=1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(6))


# #recursion: calling itself
# def hello():# this is not recursive function because there is no base condition
#     print('hello')
#     hello()

# #hello() #this is recursion but not recursive function