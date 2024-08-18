#search if a word "learning" is exist in the practice.txt 
"""
The find() method finds the first occurrence of the specified value ie return the first index of the specified value from which it starts.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
"""
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not found")

