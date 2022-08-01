for name in "python":
    print(name)

var=["Shubham","Keval","Pratik"]

for x in var:
    print(x)


#range function used to specify the range of the 2 numbers that mean's how many numbers you want to print


# for x in range(0,11):
#     print(x,end=",")

# print("\n")
# for x in range(16):
#     print(x,end=",")

# range function also take 3rd parameter that used to increment the value by the n numbers of time


# for x in range(10,0,-1):
#     print(x,end=",")

# a=["Shubham","Keval","Pratik"]
# b=["easy","hard","medium"]

# for i in a:
#     for j in b:
#         print(i,j)

for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()

for i in range(1,11):
    for j in range(i):
        print("#",end=" ")
    print()


#for Alphbet we have to add the ASCII value and then typecast the value

for i in range(1,27):
    for j in range(65,65+i):
        aa=chr(j)
        print(aa,end=" ")
    print()