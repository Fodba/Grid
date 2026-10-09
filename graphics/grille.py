from graphics.composant import Composant
from graphics.ligne import Ligne
from classes.vecteur import Vecteur
import pygame


class Grille(Composant):
    def __init__(self, parent, width, height,carte,temps) -> None:
        super().__init__(parent, width, height)
        self.type = "grille"
        self.nom = "grille"
        
        self.gridLines = []
        self.setMap(carte,temps)
        self.initGrid()
        self.setBackColor((225,0,225))
        self.grid = True
        # self.setBackColor("black")
        
    def initGrid(self):
        self.nombreColonnes = len(self.map)
        self.nombreLignes = len(self.map)
        self.largeurBloc = (self.width) / self.nombreColonnes
        self.hauteurBloc = (self.height) / self.nombreLignes
        # self.grid = grid
        self.setGrid()
    
    def setMap(self,carte,temps):
        self.map = []
        self.temps = []
        for i,col in enumerate(carte):
            self.map.append([])
            self.temps.append([])
            for j,line in enumerate(col):
                self.map[i].append(line)
                self.temps[i].append(temps[i][j])
        self.initGrid()
        
    def setPosition(self,position):
        if type(position)==(list):
            self.position = Vecteur(valeurs=[position[0],position[1]])
        elif type(position)==(Vecteur):
            self.position = position.getVecteur()
        self.rect.topleft = self.position.v[:2]
    
    # def addCell(self,position):
    #     pos = pygame.mouse.get_pos()
    #     posi = [pos[0]-self.position.v[0],pos[1]-self.position.v[1]]
    #     print(posi)
    #     print(position)
        
    def setGrid(self):
        self.gridLines = []
        for i in range(self.nombreColonnes):
            positionStart = [int((i+1) * self.largeurBloc),0]
            positionEnd = [int((i+1) * self.largeurBloc),self.height]
            lig = Ligne(self.surface,positionStart,positionEnd)
            self.gridLines.append(lig)
        for i in range(self.nombreLignes):
            positionStart = [0,int((i+1) * self.hauteurBloc)]
            positionEnd = [self.width,int((i+1) * self.hauteurBloc)]
            lig = Ligne(self.surface,positionStart,positionEnd)
            self.gridLines.append(lig)
    
    def draw(self) -> None:
        self.surface.fill(self.backColor)
        
        for obj in self.objets:
            obj.draw()
        
        radius = self.largeurBloc / 2
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                pos = [(i*self.largeurBloc),(j*self.hauteurBloc)]
                # if self.map[i][j] == 0:
                #     coeff = self.temps[i][j] if self.temps[i][j] <= 1 else 1 
                #     color = (abs(coeff*255),abs(coeff*255),abs(coeff*255))
                #     # color = "black"
                # # elif self.map[i][j] != 0:
                # else:
                coeff = self.temps[i][j] if self.temps[i][j] <= 1 else 1 
                color = (abs(coeff*255),abs(coeff*255),abs(coeff*255))
                    # color = "white"
                #     color = "white"
                    # if self.temps[i][j] == 2:
                    #     color = "green"
                    # else:
                    #     color = "blue"
                # if self.map[i][j] != 0:
                r = pygame.Rect(pos,(self.largeurBloc,self.hauteurBloc))
                pygame.draw.rect(self.surface,color,r)
                    # pygame.draw.circle(self.surface,color,pos,radius)
        
        if self.grid:
            for obj in self.gridLines:
                obj.draw()
        
        self.parent.surface.blit(self.surface,self.position.getCoordonnees())