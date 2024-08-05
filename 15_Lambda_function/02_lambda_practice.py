#lets consider this function:
def is_odd(n):
    if n%2==1:
        return True
    else:
        return False
    
#this is the function to check whether the number is odd or even and it returns True if the number is odd else False

print(is_odd(6))

#now the same function can be written by lambda function 

isodd=lambda n:n%2==1# the part n%2==1 returns True if this( n%2==1) condition is satisfied else False
print(isodd(5))