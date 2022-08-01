str="This is the String"
str1="This"
str2="10"
#capitalize() return the First letter to be Capital
print(str.capitalize())

#casefold() return the first letter to be small
print(str1.casefold())

#center() allocate the space of the given char.
print(str.center(50))

#endswith() return True if the particular string is endswith given char. otherwise return False
print(str.endswith("g"))

#index() find the index of particualr given value
print(str.index("is"))

#isdigit() return the True if Varible contain only number otherwise return False
print(str2.isdigit())

#count() return the index of particular variable
print(str.count("the"))

#isalnum() return the True if the value contain any variable and numeric but return False if it contain any special char. and white space
print(str.isalnum())

#isidentifier() return the True if the particular value is identifier
print(str.isidentifier())
print(str1.isidentifier())

#isupper() Reutrn True if the string is in Uppercase otherwise return False
print(str.isupper())

#islower() Return True if the string is in lowercase otherwise return False 
print(str.islower())

#join() is used to join the one string with the other with every word
print('-',str.join('shubham'))

#just() is used to justify the Length of the string's padding and margin
print(str.ljust(50,'/'))

#replace() return the string with the replace char.
print(str.replace("t","T"))

#swapcase() 
print(str.swapcase())