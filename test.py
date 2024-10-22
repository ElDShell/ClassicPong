import pygame
hello  = "go"
pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

is_running = True

# Load a font (None uses the default font, or you can provide a path to a .ttf font)
font = pygame.font.Font(None, 36)  # 36 is the font size
#render the text 
text = font.render(f"hello:{hello}",True,(255,255,255))

text_rect = text.get_rect(center=(480,540))

sound = pygame.mixer.Sound("")
while is_running:
    # set the back ground 
    screen.fill((0,0,0))
    for event in pygame.event.get():
        is_running= False if event.type == pygame.QUIT else True

    screen.blit(text,text_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    