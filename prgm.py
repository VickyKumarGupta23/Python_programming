d = {}
n= int(input("Enter the number of the students:--"))
for x in range(n):
    name = input("enter the roll and Name ")
    marks = input('Enter the marks')
    d[name] = marks
print(d)


for k,v in sorted(d.items()):
    print("{} name _Roll {} marks".format(k,v))