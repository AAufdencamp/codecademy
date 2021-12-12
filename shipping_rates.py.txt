
# ------------------------------------------------------------------------
# This project is a Codecademy conditional statement and boolean expression 
# exercise in the Codecademy learn Python 3 module. 
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/12
# See Readme for further details
------------------------------------------------------------------------

shipping.py

weight = 10.1

ground_premium = 125.00

#ground shipping
cost = (weight * 1.50 + 20)
if weight <= 2:
  cost = (weight * 1.50 + 20)
  print("Ground shipping will cost:")
  print(cost)
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00 + 20)
  print("Ground shipping will cost:")
  print(cost) 
elif weight > 6 and weight <= 10:
  cost = (weight * 4.00 + 20) 
  print("Ground shipping will cost:")
  print( cost)
elif weight > 10 and weight <= 22.10:
  cost = (weight * 4.75 + 20) 
  print("Ground shipping will cost:")
  print(cost)
else:
  print("Anything over 22.10 pounds will cost you the same as ground shipping premium!")  

print("Ground Shipping Premium costs a flat charge of $125.00")     

#drone shipping
cost = (weight * 4.50)
if weight <= 2:
  cost = (weight * 4.50)
  print("Drone shipping will cost:")
  print(cost)
elif weight > 2 and weight <= 6:
  cost = (weight * 9.00)
  print("Drone shipping will cost:")
  print(cost) 
elif weight > 6 and weight <= 10:
  cost = (weight * 12.00) 
  print("Drone shipping will cost:")
  print( cost)
elif weight > 10:
  cost = (weight * 14.25) 
  print("Drone shipping will cost:")
  print(cost)
else:
  print("When shipping by drone, anything over 10 pounds will cost more than ground shipping premium.")
