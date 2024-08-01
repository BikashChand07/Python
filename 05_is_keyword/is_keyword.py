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