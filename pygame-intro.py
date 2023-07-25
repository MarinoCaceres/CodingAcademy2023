import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
row_size = SCREEN_HEIGHT//3
col_size = SCREEN_WIDTH//3

BACKGROUND_COLOR = [220,220,220]
BOARD_COLOR = [10,10,10]
X_COLOR = [240,10,10]
O_COLOR = [10,10,240]

key_Q = pygame.K_q
key_W = pygame.K_w
key_E = pygame.K_e
key_A = pygame.K_a
key_S = pygame.K_s
key_D = pygame.K_d
key_Z = pygame.K_z
key_X = pygame.K_x
key_C = pygame.K_c
key_Esc = pygame.K_ESCAPE
keys_to_board = {key_Q:0,key_W:1,key_E:2,key_A:3,key_S:4,key_D:5,key_Z:6,key_X:7,key_C:8}

def convertScreenPosToRowCol(pos):
    #TODO: convert from a position [x,y] on the screen
    # to a row number and column number
    x = pos[0]
    y = pos[1]
    row = y//row_size
    col = x//col_size
    return row,col  #leave this

def convertIndexToRowCol(index):
    #TODO: convert an index in the board state list
    # into a row number and column number
    row = index // 3
    col = index % 3
    return row,col  #leave this

def convertRowColToIndex(row,col):
    #TODO: convert a row number and column number
    # into an index in the board state list
    index = 3 * row + col
    return index  #leave this

def handleMouse(pos,player1_turn,board_state):
    #TODO: update the board if needed based on where the player clicked
    # return True if it's now player 1's turn, False otherwise
    row,col = convertScreenPosToRowCol(pos)
    index = convertRowColToIndex(row,col)
    #replace this print with your code
    if board_state[index] == " ":
        if player1_turn == True:
            board_state[index] = "X"
            return False
        
        elif player1_turn == False:
            board_state[index] = "O"
            return True
    return player1_turn


def handleKey(key,player1_turn,board_state):
    #TODO: update the board if needed based on which key was pressed
    # return True if it's now player 1's turn, False otherwise
    index = keys_to_board[key]
    #replace this print with your code
    if board_state[index] == " ":
        if player1_turn == True:
            board_state[index] = "X"
            return False
        
        elif player1_turn == False:
            board_state[index] = "O"
            return True
    return player1_turn


def drawX(screen,row,col):
    #TODO: draw an X on the screen at the specified row and column
    pygame.draw.line(screen,X_COLOR,[5+(col*col_size),5+(row*row_size)],[185+(col*col_size),185+(row*row_size)],width = 10)
    pygame.draw.line(screen,X_COLOR,[185+(col*col_size),5+(row*row_size)],[5+(col*col_size),185+(row*row_size)],width = 10)
    pass 

def drawO(screen,row,col):
    #TODO: draw an O on the screen at the specified row and column
    pygame.draw.circle(screen,O_COLOR,[95+(col*col_size),95+(row*row_size)],85,width = 10)

    pass 

def drawMoves(screen,board_state):
    #TODO: draw the moves in the board state onto the screen
    # e.g. draw Xs and Os in the correct rows/columns
    for i in range(len(board_state)):
        row,col = convertIndexToRowCol(i)
        # your code here
        if board_state[i] == "X":
            drawX(screen,row,col)
        
        if board_state[i] == "O":
            drawO(screen,row,col)

def drawBoard(screen):
    #TODO: draw 4 criss-crossing lines  
    # to make the boxes where the moves go
    pygame.draw.line(screen,BOARD_COLOR,[0,200],[600,200],width = 20)
    pygame.draw.line(screen,BOARD_COLOR,[0,400],[600,400],width = 20)
    pygame.draw.line(screen,BOARD_COLOR,[200,0],[200,600],width = 20)
    pygame.draw.line(screen,BOARD_COLOR,[400,0],[400,600],width = 20)
    pass 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    player1_turn = True
    board_state = [" "]*9
    while running:
        # handle inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in keys_to_board:
                    player1_turn = handleKey(event.key,player1_turn,board_state)
                if event.key == key_Esc:
                    #TODO: reset the game to a blank board and player1's turn
                    player1_turn = True
                    board_state = [" "]*9
                    pass
            if event.type == pygame.MOUSEBUTTONUP:
                player1_turn = handleMouse(event.pos,player1_turn,board_state)
        
        #draw stuff
        screen.fill(BACKGROUND_COLOR)
        drawBoard(screen)
        drawMoves(screen,board_state)
        pygame.display.flip()

        #go to next frame
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()