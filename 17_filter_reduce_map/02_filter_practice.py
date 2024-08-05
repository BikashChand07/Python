#filter the array and return a new array with only the values equal to or above 18:
# ages=[5,12,17,18,24,32]

def age_above18(age):
        if  age >= 18:
            return True
        else:
            return False
        
print(list(filter(age_above18,[5,12,17,18,24,32])))

#using lambda function
print(list(filter(lambda age:age>=18,[5,12,17,18,24,32,23,26,10])))
