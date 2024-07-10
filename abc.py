a=input("Enter string to be encrypted:")
k=list(a)
l=[]
m=[]
for i in range (len(k)):
    if i==0:
        l.append(k(i))
    elif i%2==0:
        l.append(k(i))
    elif i%2!=0:
        m.append(k(i))
print(l)
