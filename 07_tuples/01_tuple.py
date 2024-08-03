#tuple data structure is like a list . Tuple is a ordered collection of items that contain items of any datatype like list. unlike the list , the elements of tuple cannot be modified  once it is created because of its immuatable behaviour. The immutability of Tuple makes them safer to use in certain situations where data integrity is important

'''
points to be remembered about tuples:
1)immutable: once tuple is created, its elements cannot be modified
2)ordered collection : meanings the items are stored in a specific order and can be accessed by their index
3)paranthesis : 	A tuple is represented by a sequence of values separated by commas, enclosed in parentheses
4)Memory efficient: Tuples are stored in a single block of memory, which makes them more memory efficient than lists.

'''
# tuples synatx: tuplename=(elements seperated by comma)
mytup=(1,2,3,4,5)
print(mytup) # (1, 2, 3, 4, 5)
#tuple of multiple datatype
mytup1=(1,"hello",2j,3.5,"world",[4,6,8] ,{'name':"Bikash",'rollno':12},(10,12))
print(mytup1) # (1, 'hello', 2j, 3.5, 'world', [4, 6, 8], {'name': 'Bikash', 'rollno': 12}, (10, 12))

#important:
#problem:
tup=(1)
print(type(tup)) # <class 'int'> here (1) looks like tuples but internally python treat (1) like a integer 
tup1=("hello")
print(type(tup1)) # <class 'str'>
#so remember when you store only one element in a tuple then internally it is not a tuple it is treated as the type of data that is store
#solution:
tupl=(1,)
print(type(tupl)) # <class 'tuple'> so remember when you have to store only one element in a tuple use comma after that element to make it tuple

#nested tuple:
nested_tuple=(1,("hello","world","python"))
print(nested_tuple) # (1, ('hello', 'world'))

#accessing elements of tuples:
#it is same as like a list
mytu=(1,2,3,4,5,6,7,8)
print(mytu[1]) # 2
print(nested_tuple[1][2]) # python 

#slicing 
print(mytu[1:3]) # [2, 3]

mytu[0]=10 # item assignment is not  support in tuple ie modification is not applicable in tuple because of immutable behaviour



