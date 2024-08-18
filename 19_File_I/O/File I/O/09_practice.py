#from a file containing numbers seperated by comma , print the count of even numbers.

with open("numbers.txt","r") as f:
    data=f.read()
    print(data) # 1,2,3,4,5,6,7,8,9,10,11,12
    nums=data.split(",")
    print(nums) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    count=0
    for i in nums:
        if(int(i) %2 ==0):
            count+=1

print(count)  
    
