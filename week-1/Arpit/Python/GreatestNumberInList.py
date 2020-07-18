list=[1,2,42,0,3,9,4]
largest_no= list[0]
 
for x in list:
   if x > largest_no:
       largest_no = x
 
print("Largest number is ", largest_no)