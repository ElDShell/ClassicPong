class Score():
    score = 0
    
    def add_score(self):
        self.score += 1
        
    def reset_score(self):
        self.score = 0
        
    def show_score(player1score,player2score,font,screen):
    #text
        p1text = font.render(f"Player 1: {player1score.score}",True,(255,255,255))
        p2text = font.render(f"Player 2: {player2score.score}",True,(255,255,255))
        
        #position the font
        p1text_rect = p1text.get_rect(center=(65,30))
        p2text_rect = p1text.get_rect(center=(710,30))
        
        # write the text
        screen.blit(p1text,p1text_rect)
        screen.blit(p2text,p2text_rect)
