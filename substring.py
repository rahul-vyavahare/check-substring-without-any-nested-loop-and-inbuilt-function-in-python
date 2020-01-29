x=input("enter string:")
y=input("enter substring:")
s,i,j=[],0,0
while(i<len(x)):
    if (i+j)<len(x)-1:
        if x[i+j]!=y[j]:
            i+=1
            j=0
            continue
    if j<len(y):
        j+=1
    else:
        break
if j==len(y):
    print("yes")
else:
    print("no")
