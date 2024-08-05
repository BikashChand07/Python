#Define a function that doubles the even numbers and leaves odd numbers as it is:
def double_even(num):
    if num%2==0:
        return num*2
    else:
        return num
    

#lambda function for above function :doub_even=lambda num:num*2 if num%2==0 else num
numbers=[1,2,3,4,5,6,7,8,9,10]

print(list(map(double_even,numbers))) # [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]

print(list(map(lambda num:num*2 if num%2==0 else num,numbers))) # [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]