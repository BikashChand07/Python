# "==" operator(also known as equality operator) checks  whether the values are equal or not
# "is" operator(also known as identity operator) checks whether the two variables refers to the same object .simply it checks if two varaibles refers to the value of same memory address

# Example
x=12
y=12
print(x==y) #op=True
print(x is y)# op=True

l1=[1,2,3,4]
l2=[1,2,3,4]
print(l1==l2)#op=True
print(l1 is l2) # output:False because both have same values but at different memory location. ie both refers to the different object


mylist1=[1,2,3]
mylist2=mylist1
mylist1[0]=5
print(mylist1)
print(mylist2)
print(mylist1 is mylist2)
mylist1=[1,2,3] # but now mylist1 refers to the new location with value [1,2,3] 
mylist1[1]=6
print(mylist1) # [1, 6, 3] ie mylist[1] refers to the another memory loaction with smae values like[1,2,3] but mylist2 refers to the previous location
print(mylist2) # [5, 2, 3]
print(mylist1 is mylist2)