# Function that prints out a board

from IPython.display import clear_output

def display_board(board):
    
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[7]+' | '+board[8]+' | '+board[9])

# Created a few boards to use and test
test_board = ['#','X','O','X','O','X','O','X','O','X']
sec_test = [' ',' ',' ',' ',' ',' ',' ',' ',' ','']
index_board = ['X','1','2','3','4','5','6','7','8','9']

# Function to take in a player input and assign their marker as X or O
def player_input():
    
    choice = 'wrong'
    
    #while choice is not a digit
    while choice not in ['X', 'O']:
        
        choice = input("Player 1: Please choose X or O ")
        
        if choice not in ['X','O']:
            print("Sorry I don't understand. Please choose X or O.")
        elif choice == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
 
# Function that takes in the board list object, a marker (X or O), and a desired position (1-9) and assigns it to the board
def place_marker(board, marker, position):
    
    board[position] = marker

# Function that takes in a board and a mark, to check if that mark has won
def win_check(board, mark):
    
    #vertical positions
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    # diagnoal positions
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
        print(board)
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    # horizontal positions
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True   
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True  
    else:
        return False

# Function that uses the random module to decide which player goes first 
import random

def choose_first():
    choice = random.randint(1,2)
    
    if choice == 1:
        return "Player 1"
    else:
        return "Player 2"
  
# Function returning a boolean to indicate whether a space on the board is freely available 
def space_check(board, position):
    
    if position == 1 and board[1] == ' ':
        return True
    elif position == 2 and board[2] == ' ':
        return True
    elif position == 3 and board[3] == ' ':
        return True
    elif position == 4 and board[4] == ' ':
        return True
    elif position == 5 and board[5] == ' ':
        return True
    elif position == 6 and board[6] == ' ':
        return True
    elif position == 7 and board[7] == ' ':
        return True
    elif position == 8 and board[8] == ' ':
        return True
    elif position == 9 and board[9] == ' ':
        return True
    else:
        return False

# Function that checks if the board is full and returns a boolean value    
def full_board_check(board):
          
    if board[1] != ' ' and board[2] != ' 'and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True
    else:
        return False

# Function that asks for a player's next postiion and then uses the function from step 6 to check if it's a free position, if it is then return the position for later use
def player_choice(board):
    
    # Intitial variables 
    choice = 'wrong'
    acceptable_range = range(1, 10) #range of (1-9)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input("Choose a position (1-9): ")
        
        #Digit check 
        if choice.isdigit() == False:
            print("Sorry, but you did not enter an integer. Please try again")
           
        #Range check, assume idsigit() is true
        if choice.isdigit() == True: 
            if int(choice) in acceptable_range:
                new_position = int(choice) #assign the choice as an integer to a new variable 
                within_range = True
            else:
                print("Sorry please input a number between 1 and 9")
                within_range = False #if they input anything outside of the range 
            
    # Use space_check to see if the space is true
    if space_check(board, new_position) == True:
        #return position for later use
        return new_position
    else:
        pass  
 
# Function that asks the player if they want to play again and returns a boolean 
def replay():
    
    choice = 'wrong'
    
    while choice not in ['Y', 'N']:
        choice = input("Would you like to play again? Y or N: ")
        
        if choice not in ['Y', 'N']:
            
            print("Please choose either Y or N. ")
            
    if choice == "Y":
        return True
    else:
        return False

# The actual tic tac toe game
print('Welcome to Tic Tac Toe!')        

def play_game():
                                                                                 
    game_on = True  
    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    p1, p2 = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    display_board(index_board)
    print('\nAbove displays the numbered position you may choose')
    
    while game_on == True:
        #Player 1 Turn
        if turn == 'Player 1':
            
            # Show board 
            display_board(game_board)
            
            # Choose a position
            position = player_choice(game_board)
            
            # Place marker on the position 
            place_marker(game_board, p1, position)
            
            # If player 1 wins
            if win_check(game_board, p1):
                display_board(game_board)
                print("Congrats Player 1! You've won the game!")
                
                # Ask to replay
                replay_game = replay()
                if replay_game == True:
                    game_on = True
                    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                else:
                    game_on = False
                    print('The game is over')
            else:
                
                # If it's a tie 
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw')
                    break
                    
                # If it's not a win or a tie
                else:
                    turn = 'Player 2'
        
        # Player 2 turn.
        else:
            # Show board 
            display_board(game_board)
            
            # Choose a position 
            position = player_choice(game_board)
            
            # Place marker on the position 
            place_marker(game_board, p2, position)
            
            # If player 2 wins
            if win_check(game_board, p2):
                display_board(game_board)
                print("Congrats Player 2! You've won the game!")
               
                # Ask to replay the game
                replay_game = replay()
                if replay_game == True:
                    game_on = True
                    game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                else:
                    game_on = False
                    print('The game is over')
            else:
                
                # If it's a tie
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw')
                    break
                    
                # If it's not a tie or win
                else:
                    turn = 'Player 1'

# Run the function 
play_game()
