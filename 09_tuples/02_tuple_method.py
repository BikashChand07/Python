#some methods are same like lists
tup=(1,2,3,4,5)

#index(element) method:
print(tup.index(3)) # 2 ie index(element) returns the index of specifies element

#count(element) method:
print(tup.count(4))#1 ie element 4 occurs 1 times in a tuple

#len(tuplename) method:
print(len(tup)) # 5

#append(ele) method
# tup.append(6)# no append() method in tup because it is immutable
#to use append method first convert it into list
final_tup=list(tup) # now tup is converted into list and stored in the variable final_tup
print(final_tup) # [1, 2, 3, 4, 5]
final_tup.append(6)
print(final_tup) # [1, 2, 3, 4, 5, 6]

#adding elements to the tuple using tuple concatenation
concat_tuples=(-1,0,) + tup 
print(concat_tuples) # (-1, 0, 1, 2, 3, 4, 5) ie adding (-1,0) to the tup (tuples)

#add to a tuple with unpacking:
'''
Using unpacking technique when creating a new tuple in Python, you can unpack the elements of an existing tuple into a new tuple which ideally adds elements to tuple. For example, create tuple with elements 2, 4, 6, 8, and 12. Then, created a new tuple by unpacking the elements tuples into them and adding a new element 15 at the last.

'''
tuples=(2,4,6,8,12)
print(tuples)# (2, 4, 6, 8, 12)
tuples=(*tuples,15) 
print(tuples) # (2, 4, 6, 8, 12, 15)
# The * operator is used to unpack the elements tuples into the new tuple. The result of the unpacking is a new tuple with the elements 2,4,6,8,12,15.

tuples=(0,*tuples)
print(tuples)# (0, 2, 4, 6, 8, 12, 15)