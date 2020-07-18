price=100000
credit_status= input("Select your credit status [G/B]: ")
 
if credit_status.upper() =="G":
  down_payment = 0.1* price
else:
  down_payment= 0.2*price
print("your down payment is "+str(down_payment))