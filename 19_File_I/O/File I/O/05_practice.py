'''create a new file "practice.txt" using python .Add the following data in it:
Hii everyone
we are learning File I/O
using java.
I like programming in java  '''

with open("practice.txt","w") as f:
    f.write("""
Hii everyone
we are learning File I/O
using java.
I like programming in java
            """)
    