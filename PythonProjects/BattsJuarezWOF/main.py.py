import random
import time #https://tutorial.eyehunts.com/python/add-time-delay-in-python-ms-milliseconds-1-second/#:~:text=Here%20is%20the%20answer%2C%20You%20needed%20a%20time,however%20many%20seconds%20you%20specify.%20Syntax%20time.sleep%20%28t%29?msclkid=48d2eff2c74711ec86be30c8c99ecd18
from playersClass import Myplayers
from wheelClass import Wheel


#B Welcome Introduction/Welcome Screen.
#https://textkool.com/en/test-ascii-art-generator?text=America%E2%80%99s%20game%2C%20Wheeeeeeeeeeeeeel%20of%20Fortune!

#More puzzles(copynpaste):,"Bander likes cookies","starwars is good","sponsoreder by eggslandsbest","sponsored by big onion","Will method","Love lonely","Class trip to Doctor Strange paid for by Will"
puzzleList = ["lego star wars the skywalker saga", "episode nine is the best star wars movie", "jar jar binks is the best character", "bander likes big onions", "class trip to doctor strange paid for by will"]




#Did not spend hours on any ascii art. Spent a few minutes finding some art.
print('''
 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+
 |A|m|e|r|i|c|a|s| |g|a|m|e|,| |W|h|e|e|e|e|e|e|e|e|e|e|e|e|e|e|l| |o|f| |F|o|r|t|u|n|e|!|
 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+      
''')
time.sleep(2)   #This is the make a small pause as to not overwhelm the user immediately.
print('''The world's most popular game show!
And now, from the Sony Studios,
here they are the stars of our show,
Pat Sajak and Vanna White.''')
time.sleep(2)   #Introduction to Pat Sajack

#https://oocities.org/spunk1111/men.htm?msclkid=1c61fb7ec74411ecb8ff6bc573108719
#https://oocities.org/spunk1111/women.htm?msclkid=e33fc0fcc74811ec975113b5dbdc12c6

#        .--.
#       /    |
#      ## a  a       _
#      (   '._)     |_|
#       |'-- |      | | 
#     _.\___/_   ___|_|___
#   ."\> \Y/|<'.  '._.-'
#  /  \ \_\/ /  '-' /
#  | --'\_/|/ |   _/
#  |___.-' |  |`'`
#    |     |  |
#    |    / './
#   /__./` | |
#      \   | |
#       \  | |
#       ;  | |
#       /  | |
#      |___\_.\_
#      `-"--'---'  

#Reference, easily copy the hosts
        
#       sSSSSSs
#      SS;; SSSS
#      S<   ?SSS
#       S>  SSS
#      ___)(____
#     (   \/    )
#\||, )(   (  / (
#  ||/ /\    / \ |
#   \./  )==(  / /
#       /    \//'
#      (     '|\`
#       \    /
#        \  /
#        )  ( 
#       /    \ 
#      /      |
#     /        |
#    `-........-'
#       / ) / )
#      /_/|/_/|


print('''
        .--.
       /    |
      ## a  a       
      (   '._)     
       |'-- |       
     _.\___/_   
   ."\> \Y/|<'.  |._./
  /  \ \_\/ /  '-' /
  | --'\_/|/ |   _/
  |___.-' |  |`'`
    |     |  |
    |    / './
   /__./` | |
      \   | |
       \  | |
       ;  | |
       /  | |
      |___\_.\_
      `-"--'---'  
Hello and Welcome to Wheel of Fortune!
I'm Pat Sajack, and this is Vanna White!
''')
time.sleep(1)
print('''
       sSSSSSs
      SS;; SSSS
      S<   ?SSS
       S>  SSS
      ___)(____
     (   \/    )
\||, )(   (  / (
  ||/ /\    / \ |
   \./  )==(  / /
       /    \//'
      (     '|\`
       \    /
        \  /
        )  ( 
       /    \ 
      /      |
     /        |
    `-........-'
       / ) / )
      /_/|/_/|
''')


#B Player Information

#playersDict = {}

#truenfalse=True
#while truenfalse:
  #answer=input(str("Add Player?(y/n) "))  #Continuely asks for any new players before starting. 
  #if answer == "y":   #Allows for a new player to be added. 

a=Myplayers(input(str(f"Type in Player Name: ")))
b=Myplayers(input(str(f"Type in Player Name: ")))
c=Myplayers(input(str(f"Type in Player Name: ")))

#Myplayers(input(str(f"Type in Player Name: ")))
#Myplayers(input(str(f"Type in Player Name: ")))
#Myplayers(input(str(f"Type in Player Name: ")))

playerturnList=[a,b,c]

'''counter=0
for i in range(3):
  playername=input(str(f"Type in Player {i+1} Name: "))
  if counter == 1:
    i=Myplayers(player1Name)
  
  playersDict[playername] = 0 #This adds new player name to dictionary.
  print(playersDict)  #Prints out the dictionary for testing purposes.
  #elif answer == "n":
      #truenfalse=False
'''
print("""
        .--.
       /    |
      ## a  a       
      (   '._)     
       |'-- |       
     _.\___/_   Now onto to the game with our Lucky Contestants!
""")
#Just the head of the previous character
#C creating the wheel and spinning it
# def spin():
#   global amount
  
#   #spins the wheel by getting a random value from the list
#   # amount = Wheel(random.choice(wheelList))
  
#   return Wheel.spin()

#C printing out the puzzle and having players guess
def generatePuzzle():
  global puzzle
  global blankList
   
  puzzle=random.choice(puzzleList)
  puzzleList.pop(puzzleList.index(puzzle))
  print(puzzleList)
  #INPUT RANDOM CHOICE OF CATERGORY

  # printing out the blank puzzle
  blank = "_"
  blankList = []

  for i in range(len(puzzle)):
    if puzzle[i] != " ": # if there isn't a space it appends a _ to a list 
      blankList.append(blank)
    elif puzzle[i] == " ": # if there is a space it appends the index of the puzzle
      blankList.append(puzzle[i])

def guess(player):
  global solved
  numberCorrect = 0
  followedRules = False
  vowels = ["a","e","i","o","u"]
  newBlankList = " ".join(blankList)
  print(newBlankList)
  choice = input("Would you like to: \n+ guess a letter (a)\n+ buy a vowel (b)\n+ or guess the puzzle(c): ")
  if choice == "a":
    guessLetter = input("Guess a letter: ")
    print()
    while followedRules == False:
      if guessLetter in vowels:
        guessLetter = input("Guess a letter that is NOT a vowel: ")
        print()
      else:
        followedRules = True
    #if the guessed letter is in the puzzle it replaces blanks with the letter where they belong in the phrase 
    if guessLetter in puzzle:
      for i in range(len(puzzle)):
        if guessLetter == puzzle[i]:
          blankList[i]=guessLetter 
          numberCorrect += 1
      player.score += int(amount) * numberCorrect
      print(f"{player.name} has {player.score}")
    
    else:
      print(f"Sorry there is no {guessLetter}")
  
  elif choice == "b":
    followedRules = False
    vowel = input("Which vowel would you like to buy: ")
    
    #makes the user keep guessing until they pick a vowel
    while followedRules == False:
      if vowel not in vowels:
        vowel = input("Please pick a vowel: ")
      else:
        followedRules = True
  
    if vowel in puzzle:
      for i in range(len(puzzle)):
        if vowel == puzzle[i]:
          blankList[i]=vowel
          numberCorrect += 1
      player.score += int(amount) #adds what the player spun to their total
      player.score -= 250 #subtracts what they paid for the vowel

    else:
      print(f"Sorry there is no [{vowel}]")
      print("\n")
    
  elif choice == "c":
    guessPuzzle = input("What is the puzzle? ")
    if guessPuzzle == puzzle:
      print(f"[Great job! {player} guessed the puzzle!]")
      print("\n")
      # playersDict[playername] += amount
      player.score += 1000 #adds what they got for guessing the puzzle correctly
      solved = True
      #puzzleList.pop(puzzleList.index(puzzle))
      print(puzzleList)
      return solved
      
    else:
      print("[Sorry that is not correct]")


  newBlankList = " ".join(blankList)
  print(newBlankList)
  #print('\n')



def turn(player):
  global amount
  amount=Wheel.spin(round)
  if amount=="bankrupt":
    print(f"{player} went BANKRUPT and loses a turn:\n")
    player.score = 0
    #print(player)
    return None   #This breaks out of the function early.
  
  elif amount=="Lose a Turn":
    print(f"{player} loses a turn:")
    print(player)
    return None   #This breaks out of the function early.
  
  elif amount=="car":
    print(f"{player} won a free car!!!")
  
  elif amount=="Cruise to Hawaii":
    print(f"{player} won a cruise to Hawaii!!!")

  elif amount=="Lego Star Wars":
    print(f"{player} won the best prize we have: A free copy of Lego Star Wars the Skywalker Saga for Xbox")

  else:
    print(f"{player} spun {amount}")
    guess(player)
  #print(player)

def eggCommerical():
  #https://textart.sh/topic/egg     not an artist, credits. I'm not good enough for this egg.
  #Egg commerical.  https://www.youtube.com/watch?v=CMwkT_2lBx0
  print("""Tonight's round is sponsored by 
                                                                      
                              ░░░░▒▒▒▒░░                            
                          ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
                        ▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒                      
                      ▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒                    
                    ▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒                  
                  ░░▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░                
                  ▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓                
                ▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░              
                ▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              
              ▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░            
              ▓▓▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████            
            ░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████            
            ▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒          
            ▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
            ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
          ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░        
          ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒        
          ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓████▒▒        Eggland's Best.
          ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████▓▓        
          ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████▓▓        
          ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓        
          ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▒▒        
          ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████░░        
          ░░▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████          
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████          
            ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████▒▒          
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████            
              ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████░░            
                ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████░░              
                  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████                  
                      ▒▒██████████████████████▒▒                    
                            ▒▒▓▓██████▓▓▒▒
""")
  #https://textart.sh/topic/egg
  time.sleep(2)
  print('''
  Doesn't your family deserve the best Eggland's best eggs?
  classic Cake free and Organic or Delicious farm fresh taste plus superior
  nutrition.
  ''')
  time.sleep(2)
  #There is a large reason for so many separate print's. Reason:Timing.
  print("Better Taste")
  time.sleep(1)
  print("Better Nutrition")
  time.sleep(1)
  print("Better Eggs")
  time.sleep(1)
  print("""
                       ░░░░▒▒▒▒░░                            
                   ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
                 ▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒                      
               ▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒                    
             ▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒                  
           ░░▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░                
           ▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓                
         ▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░              
         ▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██              
       ▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░            
       ▓▓▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████            
     ░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████            
     ▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒          
     ▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
     ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
   ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░        
   ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒        
   ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓████▒▒        Eggland's Best.
   ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████▓▓        
   ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████▓▓        
   ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓        
   ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▒▒        
   ▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████░░        
   ░░▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████          
     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████          
     ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████▒▒          
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████            
       ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████░░            
         ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████░░              
           ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████                  
               ▒▒██████████████████████▒▒                    
                     ▒▒▓▓██████▓▓▒▒             https://www.egglandsbest.com/
  """)


for round in range(4):
  round = 0
  solved = False
  generatePuzzle()
  eggCommerical()
  while not solved:
    for player in playerturnList:
      print(f"It's {player}'s turn")
      turn(player)
      print(f'{a.name}={a.score},{b.name}={b.score},{c.name}={c.score}\n')
  round+=1

#def finalRound():
  
   

