def hello():
    xyz="hello" #inside function => local scope
    print(xyz)

hello
#print(xyz) # error : name 'xyz' is not defined because scope of xyz is confined inside function hello

#global scope
name="shyam" #global scope/file level/ module level
print(name)


##built in scope=>print(),min(),max(),sorted() ie anywhere in python file
#global scope=> created variable within a single python file/module
#local scope=>inside function


#scope
x=5 #global scope
def hello():
    print(x) # first search x in local scope then in global scope 

hello()
