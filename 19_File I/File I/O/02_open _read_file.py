#using below synatx we dont need to close the file explicitly, python will automatically close the file after the execution of "with" block

with open("demo.txt","r") as f:
    print(f.closed)# here f.closed checks whether the file is closed or not. It returns either True or False , if file is closed it returns True else False. op = False because inside with block file will not closed
    print(f.read())
    print(f.closed)

print(f.closed)# op = True because outside the with block file will automatically closed.No need to use f.close()

with open("demo.txt","r") as f:
    for i in f: # In each iteration one line executes. 
        print(i)