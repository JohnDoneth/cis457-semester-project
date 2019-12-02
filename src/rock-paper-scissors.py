from random import randint
 
def mainMenu():
    print("Welcom to Rock Paper Scissors!\n")
    print("MENU")
    print("(1) Rules")
    print("(2) Play Game")
    print("(3) Exit\n")

    choice = input("")
     
    if choice == "1":
        print(rules())
    elif choice == "2":
        twoPlayer()
    elif choice == "3":
        endProgram()
    
def rules():
    print("RULES")
    print("Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")
     
    mainMenu()
     
def twoPlayer():
    print("Choose Rock Paper or Scissors!\n")
    player1 = input("Player 1 : ")
    player2 = input("Player 2 : ")
    print("")
     
 
    if (player1 == 'rock' and player2 == 'scissors'):
        print ("Player 1 wins.")
 
    elif (player1 == 'rock' and player2 == 'rock'):
        print ("Tie")
 
    elif (player1 == 'scissors' and player2 == 'paper'):
        print ("Player 1 wins.")
 
    elif (player2 == 'scissors' and player2 == 'scissors'):
        print ("Tie")
 
    elif (player1 == 'paper' and player2 == 'paper'):
        print ("Tie")
 
    elif (player1 == 'paper' and player2 == 'scissors'):
        print ("Player 2 wins.")
 
    elif (player1 == 'rock'and player2 == 'paper'):
        print ("Player 2 wins.")
 
    elif (player1 == 'paper' and player2 == 'rock'):
        print ("Player 1 wins.")
 
    elif (player1 == 'scissors' and player2 == 'rock'):
        print ("Player 2 wins.")
 
 
def endProgram():
     
    end = input("Would you like to end the game? (yes or no) ")
    if end == "no":
        mainMenu()
    else:
        quit()
 
mainMenu()
     
