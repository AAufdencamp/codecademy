# ------------------------------------------------------------------------
# This project is a conditional statement and boolean expression exercise.
#
# This file is part of the Codeacademy learn Python project
#
# Student: Andrea Aufdencamp
# Modified: 2021/12/12
# See Readme for further details
------------------------------------------------------------------------

import random

random_number= random.randint(1,10)
#print(random_number)

name = "Pete"
question = "Do chickens have teeth?"
answer = ''

if random_number == 1:
  answer ='Yes - definitely.'

elif random_number == 2: 
   answer = 'It is decidedly so.'

elif random_number ==3:
  answer = 'Without a doubt.' 

elif random_number ==4:
  answer = 'Reply hazy, try again.' 

elif random_number ==5:
  answer = 'Ask again later.' 

elif random_number ==6:
  answer = 'Better not tell you now.'

elif random_number ==7:
  answer = 'My sources say no.' 

elif random_number ==8:
  answer = 'Outlook not so good.'   

elif random_number ==9:
  answer = 'Very doubtful.' 

elif random_number ==10:
  answer = "Sorry, that's classified!" 

else:
  answer = 'Error'

#print(name +' asks: '+ question)

if question == " " and name ==" ":
  print("No question received. Hey, you, Magic 8-Ball needs your question!") 
elif question == " ":  
  print("Hey there, "+ name +", Magic 8-Ball needs a question first!")
elif name ==" ":
  print("Question: "+ question)
  print("Answer: "+ answer)

else:
  print(name+" asks: "+question)
  print("Answer: "+ answer) 



  



