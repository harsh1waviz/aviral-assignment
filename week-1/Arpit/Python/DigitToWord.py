digit = input("Enter digits: ")
 
digit_mapping ={
   "0": "Zero",
   "1": "One",
   "2": "Two",
   "3": "Three",
   "4": "Four",
   "5": "Five",
   "6": "Six",
   "7": "Seven",
   "8": "Eight",
   "9": "Nine"
}
 
output =""
 
for x in digit:
   output += digit_mapping.get(x) + " , "
 
print(output)