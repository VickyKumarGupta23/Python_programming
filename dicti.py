d = {}
i = int(input("Enter the  range of the key"))
for x in range(1,i+1):
    d[x] = int(input("enter the value : "))
    x = x + 1

s = sum(d.values())
print(s)    