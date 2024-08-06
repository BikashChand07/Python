# create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def print_average(self):
        sum=0
        for i in self.marks:
            sum=sum+i

        avg=(sum/3)
        return avg

s1=student("Ram",[67,78,89])
print("average of your marks is:",s1.print_average())