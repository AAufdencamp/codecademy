# ------------------------------------------------------------------------
# Python Code Challenge: Lists_2
#
# This file is part of the Codeacademy learn Python project
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/26
# See Readme for further details
------------------------------------------------------------------------

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
