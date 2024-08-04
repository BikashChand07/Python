x=5 #global scope
def hello():
    x=2#local scope
    print(x)# search x in local scope x=2

print(x)#search x in global scope x=5
hello()
print(x) # search x in global scope x=5
