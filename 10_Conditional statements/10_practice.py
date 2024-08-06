#check if a password is "Weak","Medium", or "Strong ".criteria :<6 chars(Weak),6-10 chars ("Medium"),>10 chars(Strong) 
password="123bikash"
# pasword_length=len(password)

if len(password)<6:
    print("Weak password")
elif 6<=len(password)<=10:
    print("Medium password")

elif len(password)>10:
    print("Strong password")

