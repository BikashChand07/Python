# for loop

x=[1,2,3,4,5]

for i in x:
    print(i)

#sum of all elements of x 

sum=0
for i in x:
    sum=sum+i

print(f"sum is:{sum}")

#multiplication of all elements
mul=1
for i in x:
    mul=mul*i

print(f"multiplication is: {mul}")

#input x=[1,2,3,4,5]
#output=[1,4,9,16,25]
print("practice 1")
newlist=[]
for i in x:
    newlist.append(i**2)

print(newlist)

#input x=[1,2,3,4,5]
#output=["odd","even","odd","even","odd"]
print("practice 2")
output=[]

for i in x:
    if i%2==0:
        output.append("even")
    else:
        output.append("odd")

print(output)

#practice 3:
print("practice 3")
# input=y=[11,12,24,1,2,3,1,6,2,7,1,11,19,3,8,9,3,9,10,11,12,24,1,2,3,8]
# output=[11,12,24,1,2,3,6,7,19,8,9,10] ie remove repeated elements 

y=[11,12,24,1,2,3,1,6,2,7,1,11,19,3,8,9,3,9,10,11,12,24,1,2,3,8]
ot=[]
for i in y:
    if i not in ot:
        ot.append(i)

print(ot)


#practice 4
print("practice 4")
name='Bikash Chand' 
#find no of vowels
count=0

for i in name:
    if i.lower() in "aeiou":
        count+=1

print(f"Total numer of vowels is:{count}")

#practice 5
print("practice 5")
marks={'Alan':99,'Bill':55,'corry':77}
#find the sum of marks 
sum=0
for i in marks.values():
    sum=sum+i

print(f"the sum of all students  marks is :{sum}")

#practice 6
students=['Alan','Bill','Ramesh','Corry','Ram','Shyam Bahadur','Gita']
# output= {'Alan': 4, 'Bill': 4, 'Ramesh': 6, 'Corry': 5, 'Ram': 3, 'Shyam Bahadur': 13, 'Gita': 4} ie count the number of characters and make a dictionary

dic={}
  
for i in students:
    dic.update({i:len(i)}) #adding key values to the dictionary

print(dic)

#practice 7
#input=students=['Alan','Bill','Ramesh','Corry','Ram','Shyam Bahadur','Gita']
#output:{'Alan': 0, 'Bill': 1, 'Ramesh': 2, 'Corry': 3, 'Ram': 4, 'Shyam Bahadur': 5, 'Gita': 6} ie make a dictionary with key as element of list(students) and value as their index

dict={}

for i in students:
    ind=students.index(i)
    dict.update({i:ind})

print(dict)

#range function
#  syntax:range(0,10) or range(start,end,step)
print("range function example:")
list(range(0,10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 10):
    print(i)

#practice 7 using range()
print("practice 7 question using range function")
dictionary={}
for i in range(0,len(students)):
    dictionary.update({students[i]:i})

print(dictionary)


#practice 8:
print("practice 8 question:")
us_price={'milk':2.03,'bread':2.6,'butter':2.6}#these all are US price
#convert above price into equivalent nepali price
# expected output:{'milk':267.96,'bread':343.2,'butter':343.2}
nepali_price={}
for i in us_price: #us_price contains milk , bread, butter
    nepali_price.update({i:us_price[i]*132}) # us-price[i] used to access the values using keys .here i is the key
    

print(nepali_price)

#second method
nep_price={}
for k,v in us_price.items(): #here us_price.items() provides output like: dict_items([('milk', 2.03), ('bread', 2.6), ('butter', 2.6)])
    #now in every iteration in k the key stores and in v the value stores
    nep_price.update({k:v*133.9})

print(nep_price)

us_price.items()

#practice 9
#same above question but add 13% tax to the value after calculation of nepali ruppess
with_tax={}
for k, v in us_price.items():
    with_tax.update({k:v*133.9+((13*133.9)/100)})

print(with_tax)

#practice 10
#if price<5 then add 13% tax else 20%tax
#us_price={'milk':2.03,'bread':2.6,'butter':2.6}
tax={}

for k,v in us_price.items():
    if(v < 5):
        tax.update({k:v*133.9+0.13*133.9})

    else:
        tax.update({k:v*133.9+0.20*133.9})
print(tax)