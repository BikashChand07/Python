#count positive numbers: Given a list of numbers count  how many are positive . 

numbers=[1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count=0

for i in numbers:
    if i>0:
        positive_number_count += 1

print(f"There are {positive_number_count} positive numbers in a list")
