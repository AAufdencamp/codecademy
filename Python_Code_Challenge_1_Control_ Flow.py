# ------------------------------------------------------------------------
# # Python Code Challenge #1 involving Control Flow
#
# This file is part of the Codeacademy learn Python project
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/26
# See Readme for further details
------------------------------------------------------------------------

def large_power(base, exponent):
  power = base**exponent
  if power > 5000:
    return True
  else:
      return False
    
#Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
#should print True
print(large_power(2, 12))
#should print False

#a more efficient way would be to place the operation in the if statement;
#that would remove the need for the extra variable.
