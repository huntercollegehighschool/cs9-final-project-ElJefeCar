"""
Name(s): Jeffrey Tsai and David Case
Name of Project: Escape the Cave of Jeffrey and David
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1   #uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
import os

character = input("Welcome to Escape Cave. Enter your name: ")
print("Hello", character)
print("You have been trapped inside a cave. You do not know where you are, or how you got there. You notice your surroundings, including many complex tools and two hallways, which are your only ways out. Find out how to escape, or you will remain here for the rest of eternity.")

start = input("Are you ready to begin your adventure? Type 1 to begin: ")
while start != "1":
  os.system('clear')
  print("You unfortunately don't know how to follow basic instructions.")
  start = input("Are you ready to begin your adventure? Type 1 to begin: ")

os.system('clear')
FirstTask = int(input("You're thirsty. For Task 1, you must find a reliable source of water. You have three options. Do you go for the sink (1), the toilet (2), or the mini fridge (3)? "))
while FirstTask != 3:
  os.system('clear')
  print("Wrong choice. Try again. ")
  FirstTask = int(input("You're thirsty. For your first task, you must find a reliable source of water. You have three options. Do you go for the sink (1), the toilet (2), or the mini fridge (3)? "))

os.system('clear')
SecondTask = int(input("Good choice. You find out that the mini fridge has two bottles of water left, meaning that you don't have much time. You need to get moving. On your right, you see two hallways. Seeing no other choice, you have to choose one. Hallway 1 (1) or Hallway 2 (2)? "))
while SecondTask != 1: 
  os.system('clear')
  print("Wrong choice. Try again.")
  SecondTask = int(input("You find out that the mini fridge has two bottles of water left, meaning that you don't have much time. You need to get moving. On your right, you see two hallways. Seeing no other choice, you have to choose one. Hallway 1 (1) or Hallway 2 (2)? "))

os.system('clear')
ThirdTask = int(input("Smart. Now, though, the lights have shut themselves off. The clanking footsteps on the metal behind you worsens, the scientist continually coming closer. Do you attempt to find a light switch to restore electricity (1), or continue in the dark (2)? "))
while ThirdTask != 2:
  os.system('clear')
  print("Bad decision. The scientist will find you if you try this")
  ThirdTask = int(input("Smart. Now, though the lights have shut themselves off. The clanking footsteps on the metal behind you worsens, the scientist continually coming closer. Do you attempt to find a light switch to restore electricity (1), or continue in the dark (2)"))

os.system('clear')
FourthTask = int(input("Good choice. Or maybe you're just lucky. In this hallway you come across a staircase which leads downward. On your right, there is also a door, with the words,'CONFIDENTIAL, EMPLOYEES ONLY', across it. However, to the staircase's side, the hallway continues forward and you still can't see the end of it. You have a decision to make. Do you go down the stairs (1), open the door (2), or continue down the hallway (3)? "))
while FourthTask != 2:
  os.system('clear')
  print("Wrong choice. Try again.")
  FourthTask = int(input("Good choice. Or maybe you're just lucky. In this hallway you come across a staircase which leads downward. On your right, there is also a door, with the words,'CONFIDENTIAL, EMPLOYEES ONLY', across it. However, to the staircase's side, the hallway continues forward and you still can't see the end of it. You have a decision to make. Do you go down the stairs (1), open the door (2), or continue down the hallway (3)? "))

os.system('clear')
FifthTask = int(input("The door is locked, and appears too heavy to break an opening through. Will you try to pick the lock (1), attempt to knock the door open (2), or search for a different exit (3)? "))
while FifthTask != 1:
  os.system('clear')
  print("You have to try again. You must find a way past that door.")
  FifthTask = int(input("The door is locked, and appears too heavy to break an opening through. Will you try to pick the lock (1), attempt to knock the door open (2), or search for a different exit (3)?"))

os.system('clear')
Game = 0
SixthTask = int(input("Good choice. As you open the door and enter the room, you hear the scientist behind you, chasing you down. You see another door with a 6-digit combination lock. Do you run out of the room and try to hide (1) or try to guess the password to the door(2)? "))
while SixthTask != 2 and Game != 1:
  os.system('clear')
  print("Your journey has ended. The scientist has found you.")
  Game = 1
  
  

if Game != 1:
  os.system('clear')
TotalAttempts = 0
CharacterStatus = 0
if Game != 1:
  print("You will have 3 attempts to open the door. Good luck")
while TotalAttempts <= 2 and CharacterStatus != 1 and Game != 1:
  Attempt = int(input("Enter the six-digit code (hint: use your previous answers): "))
  if Attempt == 312212:
    os.system('clear')
    print("Good job! You have escaped the cave!")
    CharacterStatus = 1
  elif TotalAttempts > 1:
    os.system('clear')
    print("Game over. You have run out of attempts and have been caught by the scientist.")
    CharacterStatus = 1
  elif Attempt != 312212:
    TotalAttempts = TotalAttempts + 1
    print("Incorrect. Number of tries remaining:", 3 - TotalAttempts)