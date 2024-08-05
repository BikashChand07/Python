'''
Datatypes:

 S.N  Data  Types	    Classes	                   Description
 1    Numeric	        int, float, complex	       holds numeric values
 2    String	        str	                       holds sequence of characters
 3    Sequence	        list, tuple, range	       holds collection of items
 4    Mapping	        dict	                   holds data in key-value pair form
 5    Boolean	        bool	                   holds either True or False
 6    Set	            set, frozenset	           hold collection of unique items
 
'''
# variables are like containers thata stores the value
a=1 #numeric datatype of integer class
b=2
# here a and b are two variables.
c="bikash" # c is string
d=False # d is a boolean
e=None #e is None ie it contains no any value
print(a+b)

#logical operators
#or
e=True or False
# print(e)
# truth table of "or"
print("True or False is ",True or False)
print("True or True is ",True or True)
print("False or True is ",False or True)
print("Flase or False is ",False or False)
print("\n")
#and 
print("True and False is ",True and False)
print("True and True is ",True and True)
print("False and True is ",False and True)
print("Flase and False is ",False and False)

print("\n")

#not 
print(not(False))
print(not(True))