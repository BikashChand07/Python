#write a recursive function to print all elements in a list.(Hint: base condition= when index exceeds length of list then stop)

li=[1,2,3,4,5]
def print_list(l,indx=0):
        if indx==len(l):
                return 0
        else:
            print(l[indx])
            print_list(l,indx+1)

print_list(li)