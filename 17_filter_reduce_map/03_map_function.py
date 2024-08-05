# help(map)
'''
syntax: map(function, iterables)
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
 You can send as many iterables as you like, just make sure the function has one parameter for each iterable.
 example:
def myfunc(a, b):
    return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
'''
#Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

def square(n):
    return n**2

print(list(map(square,[1,2,3,4]))) #[1, 4, 9, 16]
print(list(map(lambda n:n**2,[1,2,3,4]))) #[1, 4, 9, 16] using lambda function


def addition(x,y):
    return x+y

print(list(map(addition,[1,2,3],[4,5,6]))) # [1,2,3]+[4,5,6] in first iteration addition function takes two arguments ie 1 and 4 and evaluates them similarly in second iteration addition function takes argument 2 and 4 then evaluate similarly for other iteration. and finally returns the list 
