#write a recursive function to calculate the sum of first  n natural numbers
def sum_of_naturalnumber(n):
    if(n==0):
        return 0
    else:
        return sum_of_naturalnumber(n-1)+n
    
print(sum_of_naturalnumber(5))
    