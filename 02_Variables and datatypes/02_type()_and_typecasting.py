a= 23
t=type(a)
print(t) # output = <class 'int'>

b="hello"
ty=type(b)
print(ty) # output = <class 'str'>

c="21.3"
typ=type(c)
print(typ) # output =<class 'str'>

d=float(c)
print(type(d)) # "21.3"(string) is converted into float ie 21.3  . output : <class 'float'>
#example: str(21.3), int("21.3"), float(23)

print(str(21.3))
print( float(20))