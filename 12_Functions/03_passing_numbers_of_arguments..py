#passing  no of arguments as you want or numbers of positional arguments you passed
def add(*args): #supports positional arguments(add(1,2,3) and doesnot support keyword argument (add(x=2,y=3) here x and y are keyword arguments))
    print(args,type(args)) # arguments are stored in tuple

add(1,2,3,4)

#sum of arguments you passed
def sum(*args):
    s=0
    for i in args:
        s=s+i
    return s

total=sum(1,2,3,4,10)
print(f"sum of total arguments is:{total}")


