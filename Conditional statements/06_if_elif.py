#take username and password 
#if username=admin and password=123 then print "sucessfully logged in"else print " login failed"

username=input("enter username:")
password=input("enter your password:")

if username=="admin" and password=="admin123":
    print("successfully logged in")

else:
    print("login failed")


#take username , password and secret key 
#if username=admin and password=123 are matched or secretkey="secretkey123"  then print "sucessfully logged in"else print " login failed"
username=input("enter username:")
password=input("enter your password:")
secretkey=input("enter your secret key:")

if( 
    (username=="admin" and password=="admin123") 
    or 
    (secretkey=="secretkey123")
):
    print("successfully logged in")

else:
    print("login failed")


#if username and password doesnot match then only match secretkey
username=input("enter username:")
password=input("enter your password:")

if(username=="admin" and password=="admin123"):
       print("successfully logged in")
else:
    secretkey=input("enter your secret key:")
    if(secretkey=="secretkey123"): #nested if else
        print("successfully logged in")
    else:
        print("login failed.")
