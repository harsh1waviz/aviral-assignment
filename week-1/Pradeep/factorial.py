number=int(input("enter a number: "))
def fact(number):
    

    if number==0:
        return 1

    else: 
         return number* fact(number-1)
        
result=fact(number)
print(result)
