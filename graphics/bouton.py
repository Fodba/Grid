from graphics.composant import Composant
import pygame

class Bouton(Composant):
    def __init__(self, parent, width, height,texte) -> None:
        super().__init__(parent, width, height)
        self.setBackColor("grey")
        self.type = "bouton"
        self.nom = texte
        
        
        pygame.init()
        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        
        # create a text surface object,
        # on which text is drawn on it.
        self.text = self.font.render(texte, True,"black",self.backColor)
        
        # create a rectangular object for the
        # text surface object
        self.textRect = self.text.get_rect()
        
        # set the center of the rectangular object.
        self.textRect.center = self.centre.v[:2]
        
    
    
    def draw(self):
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        self.surface.blit(self.text, self.textRect)
        self.parent.surface.blit(self.surface,self.rect)