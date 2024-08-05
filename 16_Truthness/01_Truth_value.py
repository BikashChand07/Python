#The bool() function allows you to evaluate any value, and give you True or False in return
# 0,0.0,'',None,[],(),{},set(),False=> boolean value/Truthness is False and remaining are True
#simply empty ones are considered as False
print(bool(''))# False because empty string
print(bool(0)) # False 
print(bool(())) # False because empty tuple
print(bool({})) # False because empty dictionary
print(bool(set())) # False because empty set
print(bool([])) # False because empty list
print(bool(None)) #False
print(bool(0.0)) #False

print(bool('0')) #True because this is a string and not empty
print(bool([1,2]))# True because it is not empty list

