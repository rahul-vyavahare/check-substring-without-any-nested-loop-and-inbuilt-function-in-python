x=input("enter string:")
y=input("enter substring:")
s,i,j=[],0,0
while(j<len(y) and i<len(x)):
    if x[i]==y[j]:
        s.append(x[i])
        i+=1
        j+=1
        continue
    elif s!=[]:
        s=[]
        j=0
    else:
        i+=1
if j==len(y):
    print("yes")
else:
    print("no")
