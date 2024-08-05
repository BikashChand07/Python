#reduce :This function is defined in “functools” module.
#This function is useful when you need to apply a function to an iterable and reduce it to a single cumulative value
#simply reduce function takes two arguments from iterable and apply function on them , again the same function is applied on previous obtained result to the next succeding element and the procedure goes on untill no iterable elements  remaining.finally it returns one single value.
#syntax: reduce(function, iterable) iterable may be list, tuple, dictionary
''' 
working procedure:
1)At first step, first two elements of sequence are picked and the result is obtained.
2)Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
3)This process continues till no more elements are left in the container.
4)The final returned result is returned and printed on console.

example:
 For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
'''
from functools import reduce
#help(reduce)

#Example:find sum of all numbers in a list
def add(x,y):
    return x+y

sum=reduce(add,[1,2,3,4,5])
print(sum)

print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))
# print(reduce(lambda x,y,z:x+y+z,[1,2,3,4,5,6]))#error: <lambda>() missing 1 required positional argument: 'z' .Therefore remember reduce function doesnot works for more than two arguments

print(reduce(lambda m,n:m*n,(1,2,3,4)))