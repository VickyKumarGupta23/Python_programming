d = {}
s = input("enter the String")
v = {'a','e','i','o','u'}
for x in s:
    if x in v:
        d[x] = d.get(x,0)+1

print(d)

for k,v in sorted(d.items()):
    print("{} keys {} value".format(k,v))

