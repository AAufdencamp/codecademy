# ------------------------------------------------------------------------
# # Python Code Challenge #2 involving Control Flow
#
# This file is part of the Codeacademy learn Python project
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/26
# See Readme for further details
------------------------------------------------------------------------

def over_budget(budget, food_bill, eletricity_bill, internet_bill, rent):
  expenses = food_bill + eletricity_bill + internet_bill + rent
  if budget < expenses:
    return True
  else:
    return False  

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

#alternatively I could have done
#if (budget < food_bill + electricity_bill + internet_bill + rent):
 
