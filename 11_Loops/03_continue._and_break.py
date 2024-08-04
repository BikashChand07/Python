#continue
numbers=[1,2,6,8,9,6,10]
sum=0
for i in numbers:
    if i == 6:
        continue
        #skip the currently iterated item
        #doesnot run anything after continue
    sum=sum+i

print(sum)


#break
numbers=[1,2,6,8,9,6,10]
sum=0
for i in numbers:
    if i == 6:
        break # terminate/ exit from current loop
        
    sum=sum+i

print(sum)

#nested loop

names=['ram','shyam','gita','sita']
foods=['momo','chawmein','thukpa']

for i in names:
    for j in foods: #nested loops
        print(f"{i} eats {j}") # f is f-string