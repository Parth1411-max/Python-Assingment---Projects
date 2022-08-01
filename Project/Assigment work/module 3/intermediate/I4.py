

def compare(list1, list2):
    Return=False
    for x in list1:
        for y in list2:
            if x==y:
                Return=True
    print(Return)
            


l1=[11,2,1]
l2=[11,4]

compare(l1,l2)