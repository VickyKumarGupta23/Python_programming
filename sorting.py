word = input("Enter the word ")
d = {}
for x in word:
    d[x] = d.get(x,0)+1
print(d)
for v,y in sorted(d.items()):
    print(v,"keys","value:",y)    

