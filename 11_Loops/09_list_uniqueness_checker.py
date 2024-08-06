# Check if all the elements in a list are unique. If a duplicate is found ,exit the loop and print the duplicate
items=["apple","banana","orange","apple","mango"]

unique_collection=set()

for item in items:
    if item in unique_collection:
        print(f"{item} is duplicate item")
        break

    else:
        unique_collection.add(item)

# print(unique_collection)