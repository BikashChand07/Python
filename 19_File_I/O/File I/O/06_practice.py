#In a file called practice.txt replace all occurences of "java" with "python" in above file

with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("java","python")

with open("practice.txt","w") as f:
    f.write(new_data)
    
