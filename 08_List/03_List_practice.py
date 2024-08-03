# Write a program to ask the user to enter names of their 3 favorite movies and store them in a list

# movies=[]
# movies.append(input("enter your 1st favorite name:"))
# movies.append(input("enter your 2nd favorite name:"))
# movies.append(input("enter your 3rd favorite name:"))
# print(movies)

#Wap to check if a list contains a plaindrome of elements
#palindrome example: [1,2,3,2,1] this is palindrome. [1,"abc","abc",1] this is also palindrome . "MADAM" also palindrome . [1,2,3] not palindorme
#here we will use copy() method : this method returns a shallow copy of list

list1=[1,"abc","abc",1]
copy_list=list1.copy()
copy_list.reverse() 
if (copy_list==list1):
    print("given list is palindrome.")
else:
    print("not palindrome")
