info = """
Here are which letters correspond to which spaces in the game:
 Q | W | E
---|---|---
 A | S | D
---|---|---
 Z | X | C
Player 1 is X, Player 2 is O
M to restart, anything else to quit
"""

def printBoard(board):
    print("Current board: ")
    inter_row = "---|---|---"
    first_row = f" {board[0]} | {board[1]} | {board[2]}"
    second_row = f" {board[3]} | {board[4]} | {board[5]}"
    third_row = f" {board[6]} | {board[7]} | {board[8]}"
    print(first_row)
    print(inter_row)
    print(second_row)
    print(inter_row)
    print(third_row)

def getInput():
    x = input("Which space would you like to move in: ")
    if x == "Q":
        return 0
    elif x == "W":
        return 1
    elif x == "E":
        return 2
    elif x == "A":
        return 3
    elif x == "S":
        return 4
    elif x == "D":
        return 5
    elif x == "Z":
        return 6
    elif x == "X":
        return 7
    elif x == "C":
        return 8
    elif x == "M":
        return -1
    else:
        return -2
    

def handleInput(index,player1_turn,board):
    #TODO: based on the index the player decided to move in and whose turn it is,
    # modify board as needed
    # e.g.  board[index] = "X"    
    # return True if it's now player 1's turn, False otherwise
    if board[index] == " ":
        if player1_turn == True:
            board[index] = "X"
            player1_turn = False

        elif player1_turn == False: 
            board[index] = "O"
            player1_turn = True

    return player1_turn


def checkGameEnd(board):
    #TODO: BONUS.
    # Return 2 if player 2 wins
    # Return 1 if player 1 wins
    # Return 0 if the game is not over
    pass

def makeAIMove(player1_turn,board):
    #TODO: BONUS.
    # Return the index that the current player should move at.
    # v1:
    #   pick a random move
    # v2:
    #   if there is a move that immediately wins, go there
    #   otherwise, random move
    # v3:
    #   if there is a move that immediately wins, go there
    #   if there is a move that immediately wins for the opponent, block it
    #   simulate possible next moves for the opponent
    #   use that to find sequences of multiple moves that guarantee victory
    #   if there is no guaranteed victory, random move that doesn't lose
    pass

def main():
    running = True
    player1_turn = True
    board_state = [" "]*9
    while running:
        print(info)
        printBoard(board_state)
        index = getInput()

        if index == -2:
            running = False  #exit
        elif index == -1:
            #TODO: restart by resetting player1_turn and board_state
            board_state = [" "]*9
            player1_turn = True

            pass
        else:
            player1_turn = handleInput(index,player1_turn,board_state)
        


if __name__ == "__main__":
    main()