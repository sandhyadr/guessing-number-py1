import random

guessedNo = random.randint(0,9)
print(guessedNo)
count= 5
while(count>0):
      guess1 =int(input("Enter ur guess: "))
      if(guess1 == guessedNo):
         print("u guesses it right CONGRATS")
         print(guessedNo)
      else :
          print ("wrong gusee")    
      count=count-1
      
