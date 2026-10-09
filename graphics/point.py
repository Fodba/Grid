from classes.vecteur import Vecteur
from graphics.composant import Composant
import pygame


class Point(Composant):
    def __init__(self, parent, radius=5) -> None:
            super().__init__(parent, radius, radius)
            self.radius = radius
            self.backColor = "red"
            self.position += self.centre
    
    def setPosition(self,position):
        if type(position)==(list):
            self.position = Vecteur(valeurs=[position[0],position[1]])
        elif type(position)==(Vecteur):
            self.position = position.getVecteur() 
    
    def draw(self):
        # print(self.position)
        pygame.draw.circle(self.parent.surface,self.backColor,self.position.getCoordonnees(),self.radius)