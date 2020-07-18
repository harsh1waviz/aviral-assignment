name=input("Enter your name: ")
 
if len(name) < 3:
   print("Name must be more than 3 characters")
elif len(name) > 50:
   print("Name must be less than 50 characters")
else:
   print("your name is good")