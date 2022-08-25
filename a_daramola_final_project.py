#Importing random module
import random

#Title: Guess The Sssecret Number 2022 - Python Edition
print("Title: Guess The Sssecret Number 2022 - Python Edition")

#Whitespace/linebreak
print("\n")

#Created By: Akinola Daramola Jr
print("Created By: Akinola Daramola Jr")

#Whitespace/linebreak
print("\n")

#Application description
print("Application description: \n\nThis application is based on an input system.\n- Only valid inputs will progress the application forward.\n\nThis application contains an error control function.\n- In the event an input is invalid, the application will display an error message with instructions.\n\nThis application has a file creation/storage feature.\n- All valid data input is stored on file in root directory.")

#Whitespace/linebreak
print("\n")

#Game decription: "Guess the secret number to win. \nThe secret number is between 1 and 30 inclusively.\nPlayer has 5 attempt to guess the secret number correctly.\nOnly valid inputs are permissible and considered guessing attempts.\nHints are given to improve players guessing precision.\nPlayer guesses and secret number is revealed if 5th attempt is incorrect.\nGame history data can be stored in a file for viewing.\nBotth 'Play again' & 'view game history' prompts are optional.\nAre  you ready?"
print("Game description:\n\n- Guess the secret number to win. \n- The secret number is between 1 and 30 inclusively.\n- Player has 5 attempts to guess the secret number correctly.\n- Only valid inputs are permissible and considered guessing attempts.\n- Hints are given to improve players guessing precision.\n- Player guesses and secret number is revealed if 5th attempt is incorrect.\n- Player progress and game history data is stored on file for viewing.\n- Both 'play again' & view 'game history' prompts are optional.\n\nAre you ready?\n")


#Defining main() function to call startGame() function
def main():
    
    #startGame() prompts player to start game
    startGame()

    #Whitespace for formatting purposes 
    print("\n")

    #game() function starts actual game application
    game()

#Defining startGame() function
def startGame():
    
        #Prompts player to start game
        start_game = input('Press "Enter/Return" to start game...')
    
#Defining game() function which houses instructions for game application
def game():
    
    #Declaring value of secret_number variable betweeen 1 - 30
    secret_number = random.randint(1,30)

    #Initializing guesses variables to 5 guesses
    guesses = 5

    #Setting playing_game to Boolean
    playing_game = True

    #Initializing games_played variable to 0
    games_played = 0

    #Initializing games_won variable
    games_won = 0
    #Initializing games_lost variable
    games_lost = 0

    #Initializing empty player_guess list
    player_guess = []

    #While loop to keep playing_game 
    while playing_game:
        
        #Try/except block to capture IOErrors and ValueErrors
        try:
            
            #Decriments 1 unit per iteration
            guesses -= 1
            
            #Prompts user to guess secret number
            guess = int(input("Guess the secret number: "))
            
            #Stores guess value to player_guess list
            player_guess.append(guess)
            
            #If statement to control player inputs outside the range of 1 and 30
            if guess < 1 or guess > 30:
                
                #Add 1 unit to 'guesses' variable to prevents player from using invalid numbers as guess attempt
                guesses+=1
                
                #Removes invalid numbers from player_guess list
                player_guess.remove(guess)
                
                #Informs player guess is out of range and prompts player to guess between 1 - 30
                print("Out of range: Enter number between 1 - 30.")

            #Elif conditional to compare guess with secret_number value
            elif guess == secret_number:
                
                #games_played value increments 1 unit
                games_played+=1
                
                #games_won value increments by 1 unit
                games_won+=1

                #Displays message of outcome
                print("Correct! Congratulations, you win!")

                #Prompts player to play again 
                play_again = input("Would you like to play again (y/n)? ").lower()

                #If statement predicated on player input 
                if play_again == "y":

                    #playerHistory() function called to create, store and update player progress
                    playerHistory(games_played, secret_number,  player_guess)
                    
                    #Secret_number value reset to number bettween 1 - 30
                    secret_number = random.randint(1,30)

                    #Player_guess list reset to empty
                    player_guess = []
                    
                    #guesses value reset to 5 guesses
                    guesses = 5
                    
                    #Allows game to continue
                    continue
                
                #Default function if player decides not to play again.
                else:

                    #game_history prompt gives player option to view game history
                    game_history = input("Would you like to view game history (y/n)? ").lower()

                    #If statement predicated on player input
                    if game_history == 'y':

                        #gameHistory function is invoked to create, store and update game data to file
                        gameHistory(games_played, secret_number, player_guess, games_won, games_lost)

                        #Ends game
                        endGame()
                        break

                    #Default action when player does not follow view game history prompt correctly 
                    else:

                        #gameHistory() function updates game data to file
                        gameHistory(games_played, secret_number, player_guess, games_won, games_lost)

                        #Ends game
                        endGame()
                        break                        

            #elif conditional comparing player 'guesses' value with 0 after 5th attempt
            elif guesses == 0:

                #games_played value increments 1 unit
                games_played+=1

                #games_lost value increments 1 unit
                games_lost+=1

                #Displays message indicating game is over and player has lost game
                print("Game over, you lose.")

                #Displays all player guesses for that game
                print("Player Guesses:", *player_guess)

                #Displays message to player revealing the secret number
                print(f"The 'Secret Number' is  {secret_number}.")

                #Prompts player to play again
                play_again = input("Would you like to play again (y/n)? ").lower()

                #If statment predicated on player input
                if play_again == "y":

                    #createHistory function called to create, store and update data in file for each argument
                    playerHistory(games_played, secret_number,  player_guess)
                    
                    #Secret_number value reset to number bettween 1 - 30
                    secret_number = random.randint(1,30)

                    #Player_guess list reset to empty
                    player_guess = []
                    
                    #guesses value reset to 5 guesses
                    guesses = 5

                    #Allows game to continue
                    continue

                #else statement incase player decides not to play again after loss
                else:
                    
                    #game_history prompt gives player option to view game history
                    game_history = input("Would you like to view game history (y/n)? ").lower()

                    #If statement to direct player to game history
                    if game_history == 'y':

                        #gameHistory() invoked to create, store and update data to file to include games_won/lost
                        gameHistory(games_played, secret_number, player_guess, games_won, games_lost)

                        #Ends game
                        endGame()
                        break

                    #Else statement for more player flexibility in case player doesn't want to view game history 
                    else:

                        #gameHistory() invoked to create, store and update data to file to include games_won/lost
                        gameHistory(games_played, secret_number, player_guess, games_won, games_lost)

                        #Ends game
                        endGame()
                        break

            #elif statement comparing player guess value with secret_number value
            elif guess > secret_number:
                
                #Displays message to player indicating player guess was too high
                print("Incorrect. Guess is too high.")

            #else statement incase all other conditionals are not met
            else:
                
                #Displays message indicating player guess was too low
                print("Incorrect. Guess is to low.")
            
        #except ValueError: Flags all non numerical input values 
        except ValueError:
            
            #Adds 1 unit to 'guesses' variable to prevent player from using invalid values as a guess attempt
            guesses +=1
            
            #Displays Error message when input is not a valid entry 
            print("Invalid Entry: Enter a number between 1 - 30.")

        #except IOError: Flags files that do not exist in directory
        except IOError:
            
            #Displays message pertaining to file name or extension
            print('Error: File name does not exist.')

#Defining playerHistory() function creates file, stores and updates only games_played, secret_number and  player_guess values to file
def playerHistory(games_played, secret_number,  player_guess):

    #file object gameHistory.txt created in append mode and stored in variable named game_data
    with open("gameHistory.txt", "a") as game_data:

        #playerProgress() called to store current game number, secret number and all player attempts only
        playerProgress(game_data, games_played, secret_number)
        
        #Iterates through player_guess list
        for lines in player_guess:

            #findSecretNumber() called to place '√' to right of secret_number value
            findSecretNumber(lines, secret_number, game_data)

        #Writes _________ and creates a line break ("\n") on line of file for formatting purposes
        game_data.write("__________" + "\n")

#Defining gameHistory() function creates file, stores and updates data of all game history to include games_played, games_won and games_lost values to file 
def gameHistory(games_played, secret_number, player_guess, games_won, games_lost):

    #file object gameHistory.txt created in append mode and stored in variable named game_data
    with open("gameHistory.txt", "a") as game_data:

        #playerProgress() called to store current game number, secret number and all player attempts only
        playerProgress(game_data, games_played, secret_number)

        #Iterates through player_guess list
        for lines in player_guess:

            #findSecretNumber() called to place '√' symbol to right of secret_number value 
            findSecretNumber(lines, secret_number, game_data)

        #Writes _________ and creates a space ("\n") on line of file for formatting purposes
        game_data.write("__________" + "\n")

        #Creates a space ("\n") on line of file for formatting purposes
        game_data.write("\n")

        #Writes "Games Played" text with games_played value on line of file file followed by linebreaks
        game_data.write("Games Played: "+ str(games_played) + "\n")

        #Writes "Games Won" text with games_won value on line of file file followed by linebreaks
        game_data.write("Games Won: " + str(games_won) + "\n")

        #Writes "Games Lost" text with games_lost value on line of file file followed by linebreaks
        game_data.write("Games Lost: " + str(games_lost) + "\n")

        #Writes _________ and creates a linebreak ("\n") on line of file for formatting purposes
        game_data.write("__________" + "\n")

    #Displays message to player indicating game history file is being created    
    print("Creating gameHistory.txt file... file created.")

#Defining playerProgress() function writes only current game number, secret number and all player attempts to file
def playerProgress(game_data, games_played, secret_number):

    #Reserves line in file for a white space - formatting purposes
    game_data.write("\n")

    #Writes "GAME: " text with games_played value on a line of file
    game_data.write("GAME: " + str(games_played) + "\n")

    #Writes "SECRET  NUMBER: " text with secret_number value on line of file
    game_data.write("SECRET NUMBER: " + str(secret_number) + "\n")

    #Writes _________ and creates a space ("\n") on line of file for formatting purposes
    game_data.write("__________" + "\n")


#Defining findSecretNumber() - function places an '√' to the right of secret_number value in file
def findSecretNumber(lines, secret_number, game_data):
    
    #If statement comparing player_guess value and secret_number value
    if lines == secret_number:
        
        #Writes "Guess: " text and player_guess values followed by '√' symbol for matching values only on line of file
        game_data.write("Guess: " + str(lines) + " √" + "\n")

    #else write player_guess values to line of file
    else:

        #Writes "Guess: " text with player_guess values line of file
        game_data.write("Guess: " +  str(lines) + "\n")

#Defining endGame() - function prompts player with message and ends game
def endGame():
    
    #Message informing player of file status / prompting player to continue 
    message = input("Press ENTER to quit game.")
    
    #Displays message indicating game has ended
    print("Game has ended!") 
    
#Invoking main() function
main()
