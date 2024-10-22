import pygame as pg
from score import Score
# initialize the game
pg.init()

# player's scores
player1score = Score()
player2score = Score()

# set the width and height of the screen
width,height= 800,650 
screen =  pg.display.set_mode((width,height))

#set the frames of the game 
clock = pg.time.Clock()
#set the font
font = pg.font.Font(None, 36)  # 36 is the font size

# title 
pg.display.set_caption("Pong")


# Paddles
paddle_width,paddle_height = 10,100
hr = pg.Rect(
    0,
    50,
    800,
    10,
)

paddle1 = pg.Rect(
    50, # 50px from left 
    height // 2 - paddle_height //2, # Y(center of the screen - half of the rect height so it  is centered vertically)
    paddle_width, 
    paddle_height,  
)

paddle2 = pg.Rect(
    width-50-paddle_width, # width of the screen - 50 - paddle_width so it will be in the opposite dircation
    height // 2 - paddle_height //2, 
    paddle_width, 
    paddle_height, 
)
# ball 
ball_size  = 10
ball =  pg.Rect(
    width//2,
    height//2,
    ball_size,
    ball_size
)

paddle_speed = 10
ball_speed_x,ball_speed_y = 5,5
# Main game loop 
is_running = True

def reset_game(ball,paddel1,paddel2,height,width,speed):
    ball.x ,ball.y = width //2 , height //2
    speed *= -1
    
    
while is_running:
    # set the back ground 
    screen.fill((0,0,0))
    Score.show_score(player1score,player2score,font,screen)
    # to quit the game
    for event in pg.event.get():
        is_running = False if event.type ==  pg.QUIT else True
    pg.draw.rect(screen,(255,255,255),hr)
    pg.draw.rect(screen, (255, 255, 255), paddle1)  # Draw paddle 1
    pg.draw.rect(screen, (255, 255, 255), paddle2)  # Draw paddle 2
    pg.draw.ellipse(screen, (255, 255, 255), ball)  # Draw ball
    pg.display.flip() 
    
    # move the paddles
    keys = pg.key.get_pressed()
    
    if keys[pg.K_w] and paddle1.top > hr.bottom:
        paddle1.y -= paddle_speed
    if keys[pg.K_s] and paddle1.bottom < height:
        paddle1.y += paddle_speed
    if keys[pg.K_UP] and paddle2.top > hr.bottom:
        paddle2.y -= paddle_speed
    if  keys[pg.K_DOWN] and paddle2.bottom < height:
        paddle2.y += paddle_speed

    # move the ball
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # collision with top and bottom walls
    if ball.top <= hr.bottom or ball.bottom >= height:
        ball_speed_y *= -1  # Reverse the vertical direction

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1  # Reverse ball direction on collision

    if ball.right >= width:
        reset_game(ball,paddle1,paddle2,height,width,ball_speed_x) 
        player1score.add_score()
        
    if ball.left <= 0:
        reset_game(ball,paddle1,paddle2,height,width,ball_speed_x) 
        player2score.add_score()
    
    # 60fps
    clock.tick(60)  
