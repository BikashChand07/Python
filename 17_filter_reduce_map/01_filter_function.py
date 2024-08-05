#syntax: filter(function or None, iterable) .A function is run for each item in iterable
#Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true
print(filter(None,[1,2,0,False,5,'ram',{},5.5])) #<filter object at 0x0000019D95BB5D50>
#to get result convert this into list
print(list(filter(None,[1,2,0,False,5,'ram',{},5.5]))) # [1, 2, 5, 'ram', 5.5] ie returns those values for which the Truthness value is True


def isodd(n):
    return n%2==1

print(list(filter(isodd,[1,27,12,17,8,92,9,3,2,1,5])))
#print(list(filter(lambda n:n%2==1,[1,27,12,17,8,92,9,3,2,1,5]))) #using lamnda function