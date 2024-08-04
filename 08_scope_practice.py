x=5# global scope
def hello():
    global x 
    x=x+2 #x=7 but here x is global scope and x in global scope is also changed
    print(x)
    
print(x) # global x=5
hello()
print(x)# global x=7