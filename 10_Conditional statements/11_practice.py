#Determine if a year is leap year.(Leap year are divisible by 4,but not by 100 unless also divisible by 400)
#To determine if a year is a leap year, we apply a simple rule: if the year is divisible by 4, it's a leap year, except for end-of-century years, which must also be divisible by 400. For instance, the year 2000 was a leap year, while 1900 was not.
'''
A year is a leap year if “any one of ” the following conditions are satisfied: 

The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.

'''
year=2004
 
if (year%400==0) or (year%4==0 and year%100 !=0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")
