# Samirah Ali, Course #: 261, Lab title: GuessingGame

import random

print ('Guess the number!' ) 
print("")

User_Guess = 0
User_Number = -1
Guess_Count = 0

User_Number = random.randrange(1,10)
User_Number = input('Enter the limit: ')
print ("I'm thinking of a number from 1 to 10 ")
print("")

while User_Guess != User_Number:
    User_Guess = input(' Your guess: ')
    Guess_Count = Guess_Count + 1
    User_Guess = int(User_Guess)
    User_Number = int(User_Number)
    if User_Guess > User_Number:
        print('Too high.')
    if User_Guess < User_Number:
        print('Too low.')

print ('You guessed it in', Guess_Count ,'tries.')
print("")
read = (input('Would you like to play again? (y/n): '))
print("")

if read == 'n':
    print('Bye!')
elif read == 'y':
    
  User_Number = random.randrange (1,20)
  User_Number = input('Enter the limit: ')
  print ("I'm thinking of a number from 1 to 20")
  print("")
  Guess_Count = 0

while User_Guess != User_Number:
    User_Guess = input(' Your guess: ')
   
    Guess_Count = Guess_Count + 1
    User_Guess = int(User_Guess)
    User_Number = int(User_Number)
    if User_Guess > User_Number:
        print('Too high.')
    if User_Guess < User_Number:
        print('Too low.')

print ('You guessed it in', Guess_Count ,'tries.')

read = (input('Would you like to play again? (y/n): '))
print("") 

if read == 'n':
    print('Bye!')

