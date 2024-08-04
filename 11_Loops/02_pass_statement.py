#pass , continue , break
age=17
if age<18:
    pass # pass means donot execute this 

print("hello")

#practice: find sum of all numbers except 6
numbers=[1,2,6,8,9,6,10]
sum=0
for i in numbers:
    if i == 6:
        pass
    else:
        sum=sum+i

print(sum)

#second method 
# for i in numbers:
#     if number!=6:
#         sum+=number
# print(sum)


s=0
for i in numbers:
    if i == 6:
        pass
        
    s=s+i

print(s)