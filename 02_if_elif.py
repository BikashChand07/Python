#if elif else
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
if x>y:
    print(f"{x} is greater than {y}")
    print("x is greater than y")

elif x<y:
    print(f"{y} is greater than {x}")
    print("y is greater than x")

else:
    print("both are equal")