#while loop
names=['ram','shyam','gita','sita']
i=0 #initializer
while i < len(names): #condition
    print(names[i])
    i+=1 #increment or decrement

#practice1
numbers=[1,2,3,4]
i=0
sum=0
while i<len(numbers):
    sum=sum+numbers[i] #sum+=numbers[i]
    i=i+1

print(f"The sum is : {sum}")

#when to use for loop: 1) finite iteration 2) if you know how many times you are iterating
#when to use while loop: 1) infinite iteration 2) if you dont know how many times you are iterating

#practice3
#take age as  input from user untill  user gives age greater than 18

age=int(input("enter your age:"))

while age <= 18:
    age=int(input("enter your age:"))
print("welcome")