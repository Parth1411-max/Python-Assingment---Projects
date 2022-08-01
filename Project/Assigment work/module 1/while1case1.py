a= 1 
while a<=10:
    print(a,end=" ")
    a+=1
    if a==5:
        continue
    else:
        print()   

for i in range(1,11):
    if i==5:
        continue
    else:
        print(i,end=" ")