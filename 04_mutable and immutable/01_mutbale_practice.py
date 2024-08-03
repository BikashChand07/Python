mylist1=[1,2,3]
mylist2=mylist1
mylist1[0]=5
print(mylist1)
print(mylist2)
print(mylist1 is mylist2)
'''
print(mylist1) =[5, 2, 3]
print(mylist2)=[5, 2, 3] because they both refers to the same memory location
'''
mylist1=[1,2,3] # but now mylist1 refers to the new location with value [1,2,3] 
mylist1[1]=6
print(mylist1) # [1, 6, 3] ie mylist[1] refers to the another memory loaction with smae values like[1,2,3] but mylist2 refers to the previous location
print(mylist2) # [5, 2, 3]
print(mylist1 is mylist2)
