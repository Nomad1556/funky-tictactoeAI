import pygame, sys
from AiBoard import AI


pygame.init()
gAI = AI()
blank = 0
Xspace = 1
Ospace = 2

board = [[blank] *3 , [blank] * 3, [blank] * 3]
winner = False
draw_status = False
whose_turn = "Player"
font = pygame.font.SysFont(None,30)

width, height  = 400,400
screen_size = (width, height + 100)
black = 0,0,0
clock = pygame.time.Clock()
color = (0,255,255)

screen = pygame.display.set_mode(screen_size)

x_img = pygame.image.load("Assets/X.png")
o_img = pygame.image.load("Assets/o.png")

o_img = pygame.transform.scale(o_img, (130,130))

def board_init():
        draw_text()
        #Drawing vertical lines
        pygame.draw.line(screen,color,(width/3, 0), (width/3, height))
        pygame.draw.line(screen,color,(width/3 * 2, 0), (width / 3 * 2, height))
        #Drawing horizontal lines
        pygame.draw.line(screen,color,(0, height /3), (width, height /3))
        pygame.draw.line(screen,color,(0, height / 3* 2), (width, height / 3 * 2))
        pygame.draw.line(screen,color,(0, height), (width,height))

        pygame.display.update()

#Check the status of the board if we won
def check_board():
    global winner
    global draw_status
    for row in range(0,3):
        if(board[row][0] == board[row][1] == board[row][2]):
            if(board[row][0] is not blank):
                winner = True
    for col in range(0,3):
        if(board[0][col] == board[1][col] == board[2][col]):
            if(board[0][col] is not blank):
                winner = True
    if(board[0][0] ==  board[1][1] == board[2][2]):
        if(board[0][0] is not blank):
            winner = True
    elif(board[2][0] == board[1][1] == board[0][2]):
        if(board[2][0] is not blank):
            winner = True
    if(all([all(row) for row in board]) and winner is False): 
       draw_status = True

def draw():
    global whose_turn

    x,y = pygame.mouse.get_pos()
    if(x < width / 3):
        col = 1
        x_pos = 30
    elif (x < width / 3 * 2):
        col = 2
        x_pos = width / 3 + 30
    elif (x < width):
        col = 3
        x_pos = (width / 3 * 2) + 30
    else:
        col = None
    if (y < height / 3):
        row = 1
        y_pos = 30
    elif (y < height / 3 * 2):
        row = 2
        y_pos = height / 3  + 30
    elif (y < height):
        row = 3
        y_pos = (height / 3 * 2) + 30
    else:
        row = None
    if(board[row - 1][col - 1] == blank):
        board[row - 1][col - 1] = Xspace
        whose_turn = "Player"
        screen.blit(x_img,(x_pos - 10,y_pos - 15))
        draw_text()
        pygame.display.update()
    else:
        whose_turn = "Blocked"
        draw_text()

def draw_ai():
    global whose_turn

    row,col = gAI.find_best_move(board)
    if (col == 0):
        x_pos = 30
    elif (col == 1):
        x_pos = width / 3 + 30
    elif (col == 2):
        x_pos = (width / 3 * 2) + 30
    if(row == 0):
        y_pos = 30
    if(row == 1):
        y_pos = height / 3  + 30
    if(row == 2):
        y_pos = (height / 3 * 2) + 30

    board[row][col] = Ospace
    whose_turn = "AI"
    screen.blit(o_img,(x_pos - 30,y_pos -30))
    draw_text()
    pygame.display.update()

def draw_text():
    if(whose_turn == "Player"):
        msg = "It's the Player's turn"
    elif(whose_turn == "AI"):
        msg = "It's the AI's turn"
    elif(whose_turn == "Blocked"):
        msg = "That space is taken! Try again"
    screen.fill((0,0,0), (0,401,400,100))
    txt1 = font.render(msg, True, color)
    text1_r = txt1.get_rect(center =(width/2, 500-50))
    screen.blit(txt1,text1_r)
    pygame.display.update()

def winning_screen():
    if(draw_status):
        msg = "It's a draw! Press k to play again"
    elif(whose_turn == "AI"):
        msg = "AI won! Press k to play again"
    elif(whose_turn == "Player"):
        msg = "You won! Press k to play again"
    screen.fill((0,0,0), (0,401,400,100))
    txt1 = font.render(msg, True, color)
    text1_r = txt1.get_rect(center =(width/2, 500-50))
    screen.blit(txt1,text1_r)
    pygame.display.update()

def reset_board():
    global winner
    global whose_turn
    global blank
    global draw_status
    screen.fill((0,0,0))
    board_init()
    winner = False
    draw_status = False
    for row in range(0,3):
        for col in range(0,3):
            board[row][col] = blank
    whose_turn = "Player"
    draw_text()
    main()

def main():
    global winner
    while not winner and not draw_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type is pygame.MOUSEBUTTONDOWN:
                draw()
                if(whose_turn == "Blocked"):
                    break
                check_board()
                if(winner == True or (draw_status == True)):
                    break
                draw_ai()
                check_board()
                if(winner == True or (draw_status == True)):
                    break
        pygame.display.update()
        clock.tick(30)
    while winner or draw_status:
        winning_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    reset_board()
        pygame.display.update()
        clock.tick(30)
board_init()
main()

