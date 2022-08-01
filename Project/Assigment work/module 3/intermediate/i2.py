list1=[1,2,3,4]
list2=[2,3,4]
new_list=[]

for x in list1:
    if x not in list2:
        new_list.append(x)

print(new_list)