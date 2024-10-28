class Player():
    def __init__(self,name):
        self.name = name
        self.score = 0
    
    def add_score(self):
        self.score += 1
        
    def reset_score(self):
        self.score = 0
def show_players_score(player1,player2,font,screen):
#text
    p1text = font.render(f"{player1.name}: {player1.score}",True,(255,255,255))
    p2text = font.render(f"{player2.name}: {player2.score}",True,(255,255,255))
    
    #position the font
    p1text_rect = p1text.get_rect(center=(65,30))
    p2text_rect = p1text.get_rect(center=(710,30))
    
    # write the text
    screen.blit(p1text,p1text_rect)
    screen.blit(p2text,p2text_rect)
