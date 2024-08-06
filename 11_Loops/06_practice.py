#calculate the sum of even numbers up to a given number n
n=10
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i

print(f"Sum of even numbers up to {n} is {sum}")