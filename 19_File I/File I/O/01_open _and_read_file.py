#syntax: open("file name","mode") # mode = read(r) = by default, write(w), append(a), binary mode(b) ,opening a text file updating(+ )
f = open("demo.txt","rt")
# data=f.read()# f.read(2) it reads only first 2 characters
#f.readline() # reads  only one line at a time
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
# print(data)
f.close()