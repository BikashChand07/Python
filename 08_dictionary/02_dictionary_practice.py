x={
    "id":1,
"name":"ram"
}
# y=x  since x is a dictionary ie  mutable object so when we assign y with x after that if we change the data of x or y it will change the contents of both x and y so to avoid this use copy method
y=x.copy()
y['email']="abc@gmail.com"
print(x)
print(y)
#output:
# {'id': 1, 'name': 'ram'}
#{'id': 1, 'name': 'ram', 'email': 'abc@gmail.com'}