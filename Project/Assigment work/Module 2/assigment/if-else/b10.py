i=int(input("Enter the value:"))
fact=1

if i<0:
    print("Number is Neagative:")
elif i==0:
    print("Number is zero")
else:
    for i in range(1,i+1):
        fact=fact*i
print(fact)

