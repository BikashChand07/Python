#WAp to count the numbers of students with the grade "A"  in the following tuples
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))

#store the above values in a list and sort them from "A" to "D" ie in ascending order
grade_list=list(grade)
grade_list.sort() # by default sort in asscending order
print(grade_list) # ['A', 'A', 'A', 'B', 'B', 'C', 'D']

#sort in descending order
grade_list.sort(reverse=True)
print(grade_list) # ['D', 'C', 'B', 'B', 'A', 'A', 'A']