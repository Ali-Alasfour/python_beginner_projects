# defining variables and importing modules
import random
playerscore = 0 
computerscore = 0
# functions
def turnplayer():
    totalPoints = 0
    turnpoints = 0
    choice = 1
    if choice == 1:
        while choice == 1:
            print("would you like to take a turn (1)yes (2)no")
            choice = int(input())
            dicesquare = random.randint(1,6)
        if dicesquare == 1:
            print("you rolled a zero")
            turnpoints = 0
        else:
            print(f"your rolled a {dicesquare}")
            turnpoints += dicesquare
            print(totalPoints)
    else:
        totalPoints += turnpoints
   
    
        
#introduction
print("The Pig Game is a classic and easy-to-play dice game that can be enjoyed by people of all ages. It's a game of chance and strategy that involves rolling a single die to accumulate points while avoiding the risk of losing all your points and going pig. The objective of the game is to be the first player to reach a set number of points, typically 100, although this can vary based on the rules you choose to follow.")
gamemode = input("single player(1) or multiplayer(2)::::")

#main

# while playerscore or computerscore >= 100:

    

