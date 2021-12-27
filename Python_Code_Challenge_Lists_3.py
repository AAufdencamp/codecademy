# ------------------------------------------------------------------------
# Python Code Challenge: Lists_3
#
# This file is part of the Codeacademy learn Python project
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/26
# See Readme for further details
------------------------------------------------------------------------

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else: 
    return lst2[-1]  

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
