list=[1,2,1,2,3,4,5,4,5,6,7,8,9]
unique= []
 
for x in list:
   if x not in unique:
       unique.append(x)
 
print (unique)