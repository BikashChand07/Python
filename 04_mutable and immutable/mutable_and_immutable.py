# mutable and immutable datatypes in python
# mutable datatypes or objects = List, Dictionaries, set . These are objects whose values can be altered post their creation. or simply we can say that the value of mutable objects can be altered after the creation.
# immutable datatypes or objects = Number, Boolean, String, Tuple. cannot be altered once it’s been established.

# Despite having distinct characteristics, mutable and immutable objects can coexist within the same data structure. For instance, a tuple (which is immutable) can contain a list (which is mutable). This forms an intriguing dynamic where the tuple’s elements remain constant, but the list’s elements can be altered. 
#Example:
'''
Tuple containing a list
my_tuple = (1, 2, ['a', 'b'])

#The list element within the tuple can be modified
my_tuple[2][0] = 'c'  # The tuple now becomes (1, 2, ['c', 'b']) #this is how the mutable and immutable objects coexist
'''

#immutable:
#string
username="Bikash" #now the username refers to the value Bikash
# print(username) #output= Bikash
username="chand" #Any modification results in a new string object. ie initially username refers to the Bikash value and when the value "chand " is created and refered by the username then the previous link between username and Bikash is deleted ie the Bikash value is deleted from the memory and the username points the new value ie Chand
#It means when a modification is done then the new string object is created and previous one is removed by memory management of python
# print(username) #output = chand . It seems like change in value. Actually there is no change, interally the first reference is deleted and new reference is created that holds the value "chand"

#int
# Attempting to alter the value of an integer results in the creation of a new object
x=10
y=x
# print(x) # op=10
# print(y)# op=10
# print(id(x)==id(y)) # True ie both x and y refers to the same memory location
#lets change the value of x and check whether it alters the value of y or not
# print("After changing the value of x :")
# x=20
# print(x)#op=20
# print(y)#op=10
# print(id(x)==id(y))
#initially x and y refers to the same value ie 10. when the value of x is changed the x points to the new value but y points to the same previous value. so x =20 and y=10. ie change in x doesnot reflect changes in y . therefore int is immutable.

#Tuples: synatx: variablename=(1,2,3)
#Because Tuples in python are immutable by nature, we are unable to add or modify any of their contents. if we do modification then it will throw error. Example:
tup=(1,2,3,4)

#trying to modify the tuple object
tup[1]=5
print(tup) # error will generate.  Error like: TypeError: 'tuple' object does not support item assignment


#mutable: 

#list
mylist=[1,2,3,4]
newlist=mylist

# Checking if the two variables point to the same memory location
print(id(mylist)==id(newlist)) #op=True it both(mylist and newlist) points to the same value(ie same memory address)

print(mylist) #op=[1, 2, 3, 4]
print(newlist) #op=[1, 2, 3, 4]

#modifying the mylist

mylist[2]=5
print(mylist) # op= [1, 2, 5, 4]
print(newlist) # op=[1, 2, 5, 4]
print(id(mylist)==id(newlist)) #returns True because both mylist and newlist points to the same memory address and content of both list gets changed.
#when we modify the content of mylist the newlist also get changed because both mylist and newlist points to the same memory address . unlike mutable dataypes there is no creation of new object whenever the existing object is changed or modified.

#2 Dictionary:
dic={1:'a' ,
      2:'b',
      3:'c',
      4:'d'
    }

print("The original dictionary is: ",dic) # The original dictionary is:  {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#changing the content of dictionary
dic[3]='hello'# dic[key] = new_value

print("The modified dictionary is:", dic) #the modified dictionary is: {1: 'a', 2: 'b', 3: 'hello', 4: 'd'}



