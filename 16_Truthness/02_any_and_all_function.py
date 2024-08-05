#any(iterable) here iterable may be list, tuple, dictionary.If any of the Boolean Value is True then this method returns True else returns False .The any() function returns True if any item in an iterable are true, otherwise it returns False.
#all(iterable) if all of the Boolean value is True then only this function returns True else returns False

value=any([0,'',None,[],(),{},set(),False])
print(value) # False beacuse all the values are False

val=any([0,'',None,[],(),{},set(),False,"abc"])
print(val) # True because one of the value is True and we know that if any of the value is true then any() method returns True Value

va=all([0,'',None,[],(),{},set(),False])
print(va)# false beacuse all values are False

v=all(['0',(1,2),{'name':'Bikash'},[4,5],"abc",2])
print(v)#True because all values have True boolean values