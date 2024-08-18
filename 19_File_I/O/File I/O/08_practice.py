#write a function to find in which line of the file does the word 'learning' occur first.print -1 if word not found

def find_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:

        while data: # runs for only valid data . not for invalid data(like \n)
            data=f.readline()
            if(word in data):
                print(f" The word {word} is found in line number {line_no}")
                return 
            line_no+=1

    return-1

find_line()

