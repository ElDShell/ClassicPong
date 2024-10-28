import pygame as pg
import random
from player import Player,show_players_score

# set the width and height of the screen
width,height= 800,650 
# paddels    
paddle_width,paddle_height = 10,100

# ball
paddle_speed = 10

ball_size  = 10
#colors
BLACK = (0,0,0)
BLUE = (0,0,225)
WHITE = (225,225,225)
GRAY = (30,30,30)

# to make the random between 5 and -5 so the ball start moving in differnet direction at the start of the game
ball_speed = {5,-5}



def reset_game(ball,speed):
    ball.x ,ball.y = width //2 , height //2
    speed *= -1
    
def start_game(player1, player2):
    # Initialize the game
    pg.init()
    screen = pg.display.set_mode((width, height))
    hr = pg.Rect(0, 50, 800, 10)

    # Paddles and ball setup
    paddle1 = pg.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
    paddle2 = pg.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
    ball = pg.Rect(width // 2, height // 2, ball_size, ball_size)

    # Sound effect
    collision_sound = pg.mixer.Sound("assets\collision sound.mp3")
    clock = pg.time.Clock()
    font = pg.font.Font(None, 36)
    
    # Button setup
    button_position = (350, 250)
    button_size = (100, 50)  # Width, Height adjusted for better visibility
    button_rect = pg.Rect(button_position, button_size)
    
    # Game state variables
    show_button = True
    round_active = False
    ball_speed_x, ball_speed_y = random.choice(list(ball_speed)), random.choice(list(ball_speed))
    is_running = True

    while is_running:
        # Fill background
        screen.fill(GRAY)
        pg.draw.rect(screen, WHITE, hr)  # Draw HR
        show_players_score(player1, player2, font, screen)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                pg.quit()
            
            # Show and handle button click only if a round isn't active
            if show_button and not round_active:
                show_button, round_active = start_round(screen, button_rect, BLUE, font, event)
        
        # Draw the start button if it's supposed to be visible
        if show_button and not round_active:
            pg.draw.rect(screen, BLUE, button_rect)
            button_text = font.render("Start Round!", True, WHITE)
            text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, text_rect)

        # Game logic if round is active
        if round_active:
            # Draw paddles and ball
            pg.draw.rect(screen, WHITE, paddle1)
            pg.draw.rect(screen, WHITE, paddle2)
            pg.draw.ellipse(screen, WHITE, ball)

            # Move paddles
            keys = pg.key.get_pressed()
            if keys[pg.K_w] and paddle1.top > hr.bottom:
                paddle1.y -= paddle_speed
            if keys[pg.K_s] and paddle1.bottom < height:
                paddle1.y += paddle_speed
            if keys[pg.K_UP] and paddle2.top > hr.bottom:
                paddle2.y -= paddle_speed
            if keys[pg.K_DOWN] and paddle2.bottom < height:
                paddle2.y += paddle_speed

            # Move ball
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            # Ball collision with walls
            if ball.top <= hr.bottom or ball.bottom >= height:
                ball_speed_y *= -1
                collision_sound.play()
            if ball.colliderect(paddle1) or ball.colliderect(paddle2):
                ball_speed_x *= -1
                collision_sound.play()

            # Reset game if ball is out of bounds
            if ball.right >= width:
                reset_game(ball, ball_speed_x)
                player1.add_score()
                show_button, round_active = True, False
            elif ball.left <= 0:
                reset_game(ball, ball_speed_x)
                player2.add_score()
                show_button, round_active = True, False

        # Update display once per frame
        pg.display.flip()
        clock.tick(60)


def start_round(screen,button_rect,color,font,event): 

    pg.draw.rect(screen,color,button_rect)
    # button text
    button_text = font.render("Start!!",True,BLUE)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)
    pg.display.flip()

    if event.type == pg.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            print("Button clicked")
            return False,True
    return True,False