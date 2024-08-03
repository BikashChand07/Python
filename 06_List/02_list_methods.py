#list methods
x=[1,2,3,4]
print(sum(x)) #add all the elements of the list
print(min(x)) #returns the minimum from list
print(max(x))
print(len(x)) #find the number of elements in list or length of list
print(sorted(x)) #sort the list in asscending order
print(sorted(x, reverse=True)) #sort the list in descending order

#append(element) method:
x.append(5) #append(element) method takes only one argument , it appends only one element to the last of list
print(x)

# insert(index,element) method used to insert element at given index and shift the element to  the right and it increase the size of the list
x.insert(1,"hello")
print(x)

#remove(element) method: removes the first occurence of element
x.append("hello")
print(x) #[1, 'hello', 2, 3, 4, 5, 'hello']
x.remove("hello")# in the list there are two hello strings , remove method removes the firts hello strings from list
print(x) # [1, 2, 3, 4, 5, 'hello']

#pop(index) method : removes element of given  index
#before pop: [1, 2, 3, 4, 5, 'hello']
x.pop(5) #pop(5) method removes the element of index 5th from list
print(x) # [1, 2, 3, 4, 5]

#count(element) method:
# count(element) method : returns the number of occurence of element given to the count method
x.append(2) 
print(x)#[1, 2, 3, 4, 5, 2]
print(x.count(2)) # in the list the element 2 is occured two times so the count(2) method returns 2
print(x.count(3))# 1 ie 3 occurs only one time in list

# index(ele, beg, end) : This function returns the index of first occurrence of element after beg and before end
print(x.index(2,4,6)) # it returns  5 because from begining index ie 4 and ending index 6 the element 2 occurs at the index 5 so it returns 5

#there is no any specific update method in list. but there are many ways to update the list like slicing ,append , extend and others
#updating the list using slicing:
print(x) #  before update:[1, 2, 3, 4, 5, 2]
x[1:3]=["hello","world"] # here slicing the elements from index 1 to 3 returns the element of index 1 to elements of index 2 ie[2,3] but not include element of index 3
print(x) # after update: [1, 'hello', 'world', 4, 5, 2]

#extend([el1,el2,el3,..]) method
x.extend([6,7,8]) # here extend method adds the elements from the last of list  
print(x)


