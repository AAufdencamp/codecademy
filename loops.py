# ------------------------------------------------------------------------
# This is an exercise control flow with loops.
#
# This file is part of the Codeacademy learn Python project
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/22
# See Readme for further details
------------------------------------------------------------------------

# Your code below:
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares =[]

for num in single_digits:
    print(num)
    squares.append(num**2)

print(squares)   

cubes =[num**3 for num in single_digits]

print(cubes)
