#list in python is a mutable datatypes or datastructures
#list is like an array in other programming language, but list can store multiple different types of values.
mylist=[1,2,3,4,5]
mylist1=[1,1.2,"Ram",2j,"True",(1,2,3),{'name':"bikash",'rollno':12}] 
#here mylist1 contains integer, float,string,boolean,set and dictionary datatypes
print(mylist1[3])
print(mylist1[4])
print(mylist1[5])
print(mylist1[6])

#slicing in list: syntax=mylist[startindex:endingindex:steps] # steps is optional
print(mylist[0:2]) #it will return the element of index 0 ,1 but excluding the element of index 3
print(mylist[0:]) #it will return element of 0th index to last index including last element
print(mylist[:len(mylist)])# here starting index is assumed as 0th
print(mylist[:])

#list comprehension
# for i in range(0,10):
#     i=i**2
#     print(i)

li=[i**2 for i in range(0,10) ] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(li)