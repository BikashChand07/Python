#Given a string ,find the first non repeated character

str="teexteracdcdc"

for char in str:
     if str.count(char)==1: 
          print(f"First non repeated character is :{char}")
          break
          
