# numbers = decimal,fraction,complex,integer, boolean also treated as numbers(1=True,0=False) and set also treated as number internally and  many more
x=2
y=3
z=4
# print(x,y,z) # output : 2 3 4 this is like tuple representation
# print(x+1,y*3) #output : 3 9
# print(2**3) # output : 8 (2^3)

# print(repr('Bikash')) #output : 'Bikash' ie it prints as it is  


#important
print(2<3<5) # output= True . actually the statement 2<3<5 is looks like this internally 2<3 and 3<5 (ie True and True ie True)
print(2<3<1) #output=  False. 2<3 and 3<1 which is true and false ie false here and = logical and
print(1==2<3) #output = false. 1==2 and 2<3 which is false and true ie final output = false

#import library called math
import math
print(math.floor(2.3))# output=2 floor provides closest number  below value ie here 2 is the closest below value to the 2.3 simply floor returns the small value relative to the provided number
print(math.floor(-3.5)) #output = -4
print(math.trunc(2.8)) #output = 2 . trunc() returns the closest value towards zero
print(math.trunc(-3.5))#output = -3

print(int('64',8)) # that means convert 64 into octal(here 8 represents the octal). output=52
print(int('64',16))# converts 64 into hexadecimal(16) output=100

#import random library

import random
print(random.random())# generates random number
print(random.randint(1,10)) # provides random integer between 1 to 10

mylist=['Ironman','Thor','Captain America','Black Panther'] # list of superheroes
print(random.choice(mylist)) # generates the random values from the provided list

#shuffle method of random library . example : While  playing cards we need shuffle (rearrange the values or cards).
random.shuffle(mylist)
print(mylist)

#problem 
print(0.1+0.1+0.1-0.3) # expected output =0.0 but actual output=5.551115123125783e-17( this result is wrong)
print((0.1+0.1+0.1)-0.3) # expected output =0.0 but actual output=5.551115123125783e-17( this result is wrong)
#solution : import Decimal library from decimal
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')) # output=0.0

#set also can be represented as number
setone={1,2,3,4}
print(setone)# ouptut={1, 2, 3, 4}
#set operation: union(or ie '|'), intersection(and ie '&'), difference(-)
#union
settwo={5,6}
print(setone|settwo) # output={1, 2, 3, 4, 5, 6}
#intersection
setthree={1,3,6}
print(setone&setthree)#output={1, 3}
print(setone&settwo) # output :set(). It returns the empty set because there is no any common element between setone and settwo and the empty set is represented by :set() in python. In mathematics empty set is represented by {} but in python {} represents the empty dictionary.
print(type({})) #output :<class 'dict'>
print(type(set())) # output:<class 'set'>

print(True==1) #output=True
print(False==0) #output=True
print(True is 1)# output= False because in memory true and 1 are treated as different objects so it returns false. "is" returns true if both the value and object is same

