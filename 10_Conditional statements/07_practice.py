#classify a persons age group  : child(<13), teenager(13-19), Adult(20-59), senior(60+)

age=int(input("enter your age:"))
if age<13:
    print("child")
elif 13<=age<=19:
    print("teenager")

elif 20<=age<=59:
    print("Adult")
    
else:
    print("senior")