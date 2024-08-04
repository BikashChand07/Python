x=5 #global scope
def hello():
    y=x+2# y is local scope but search x in local scope and x is not found in local scope then search x in global scope where x is 5 
    print(y)# search y in local scope y=7

print(x)#search x in global scope x=5
hello()
print(x) # search x in global scope x=5