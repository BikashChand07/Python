
def calculation(x,y):
    addition=x+y
    subtraction=x-y
    multiplication=x*y
    print(f"The sum is:{addition}")
    print(f"The difference is:{subtraction}")
    print(f"The product is:{multiplication}")

calculation(4,2)


#with return statement...
def calculation(x,y):
    addition=x+y
    subtraction=x-y
    multiplication=x*y
    return addition # after this return statement the control comes out of function and no further return statement runs so only addition will return
    return subtraction
    return multiplication 

calculation(4,2)