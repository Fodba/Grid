from classes.vecteur import Vecteur
import pygame


class Composant:
    def __init__(self,parent,width,height) -> None:
        self.parent = parent
        self.type = "composant"
        self.nom = "composant"
        self.surface = pygame.Surface((width,height))
        self.rect = self.surface.get_rect()
        self.size = Vecteur(2)
        self.width,self.size.v[0] = width,width
        self.height,self.size.v[1] = height,height
        self.centre = (self.size) / 2
        self.position = Vecteur(2)
        self.rect.center = self.position.v[:2]
        self.color = "black"
        self.backColor = "white"
        self.surface.fill(self.backColor)
        self.objets = []
        
    def setSize(self,width,height):
        self.width = width
        self.height = height
        
    def setColor(self,color):
        self.color = color
        
    def setPosition(self,position):
        if type(position)==(list):
            self.position = Vecteur(valeurs=[position[0],position[1]])
        elif type(position)==(Vecteur):
            self.position = position.getVecteur()
        self.rect.center = self.position.v[:2]
        
    def setBackColor(self,backColor):
        self.backColor = backColor
        self.surface.fill(self.backColor)
    
    def draw(self):
        self.parent.surface.blit(self.surface,self.rect)