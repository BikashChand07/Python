#function:
def addition(): # function definition
    x=1
    y=2
    sum=x+y
    print(sum)

addition() #function call /run / execute

def addition(x,y): #x and y are positional arguments/parameters
    sum=x+y
    print(sum)

addition(2,3) # or addition(x=2,y=3) or addition(2,y=3) or addition(y=3,x=2)  but addition(x=2,3) is not valid because positional argument follows keyword argument

def addition(y,x=0):
    sum=x+y
    print(sum)  #return None

addition(2) # here y is assign with 2 and x=0

#................................

#return from function
def addition(x,y):
    sum=x+y
    return sum #return sum

add=addition(2,3)
print(add)

#..................
def addition(x,y):
    # documentation string or doc string
    """ add two numbers x and y and return its sum"""
    sum=x+y
    return sum #return sum

add=addition(2,3)
print(add)
help(addition)

#returns multiple values from function
def calculation(x,y):
    addition=x+y
    subtraction=x-y
    multiplication=x*y
    return addition , subtraction, multiplication # returns value in tuple 

calculation(4,2)

#tuple unpacking
addition,subtraction,multiplication=calculation(4,2)
print(addition,subtraction,multiplication)

#supports any number of keyword arguments
def addition(**kwargs): # data stored in dictionary format  like {'x': 2, 'y': 3, 'z': 4}
    print(kwargs,type(kwargs))

addition(x=2,y=3,z=4)

#......

def addition(**kwargs):
    sum=0
    for i in kwargs.values():
        sum=sum+i

    return sum

add=addition(x=1,y=2,z=3)
print(add)

#positional and keyword argunents
def addition(*args,**kwargs): #positional arguments+keyword arguments
    sum=0
    for i in args:
        sum=sum+i
    
    for i in kwargs.values():
        sum=sum+i

    return sum

addition(3,4,5,x=1,y=2,z=3)



#....
def factorial(num):
    fact=1
    for i in range(2,num+1): # for i in range(n,0,-1) ie range(start,stop,step)
        fact=fact*i

    return fact

f=factorial(5)
print(f)