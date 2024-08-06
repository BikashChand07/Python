#Movie tickets are priced based on age :$12 for adults (18 and over) $8 for childern.Everyone gets a $2 discount on wednesday 

age=10
day="wednesday"

price=12 if age>=18 else 8
# print(price)

if day=="wednesday":
    price=price-2

print("your ticket price after discount is: $",price)