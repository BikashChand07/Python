#Multiplication_table_printer: print the multiplication table for a given number up to 10,but skip the fifth iteration
num=3
for i in range(1,11):
    if i==5:#detection of fifth iteration
        continue # skip the fifth iteration
    
    print(f"{num} x {i} = {num*i}")