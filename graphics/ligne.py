from graphics.composant import Composant
from classes.vecteur import Vecteur
import pygame


class Ligne(Composant):
    def __init__(self, parent, pt1, pt2) -> None:
        self.epaisseur = 2
        super().__init__(parent, 2, 2)
        # self.surface = None
        self.origine = Vecteur(2)
        self.fin = Vecteur(2)
        if type(pt1) == (list):
            v = Vecteur(valeurs=pt1)
            self.origine = v
        elif type(pt1) == Vecteur:
            self.origine = pt1
        if type(pt2) == (list):
            v = Vecteur(valeurs=pt2)
            self.fin = v
        elif type(pt2) == Vecteur:
            self.fin = pt2
        self.setBackColor("black")
        
    def setPosition(self,point,position):
        if type(position)==(list):
            point = Vecteur(valeurs=[position[0],position[1]])
            point -= self.centre
        elif type(position)==(Vecteur):
            point = position.getVecteur() - self.centre
        return point
    
    def draw(self):
        pygame.draw.line(self.parent,(self.backColor),self.origine.getCoordonnees(),self.fin.getCoordonnees(),self.epaisseur)