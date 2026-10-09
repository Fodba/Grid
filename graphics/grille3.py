from graphics.composant import Composant
from graphics.ligne import Ligne
from classes.vecteur import Vecteur
import pygame


class Grille(Composant):
    def __init__(self, parent, width, height,carte,type=None) -> None:
        super().__init__(parent, width, height)
        self.type = "grille"
        self.nom = "grille"
        
        self.unique = False
        self.type = 0
        if type is not None:
            self.unique = True
            self.type = type
        
        self.gridLines = []
        self.setMap(carte)
        self.initGrid()
        self.setBackColor((225,0,225))
        self.grid = False
        # self.setBackColor("black")
        
    def initGrid(self):
        self.nombreColonnes = len(self.map)
        self.nombreLignes = len(self.map)
        self.largeurBloc = (self.width) / self.nombreColonnes
        self.hauteurBloc = (self.height) / self.nombreLignes
        # self.grid = grid
        self.setGrid()
    
    def setMap(self,carte):
        self.map = []
        for i,col in enumerate(carte):
            self.map.append([])
            for j,line in enumerate(col):
                self.map[i].append(line)
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
        if len(self.map) > 0:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    # print(i)
                    # print(j)
                    # print(self.map[i][j])
                    # if self.map[i][j] >= 1 : self.map[i][j] = 1
                    # if self.map[i][j] <= -1 : self.map[i][j] = 0
                    pos = [(i*self.largeurBloc),(j*self.hauteurBloc)]
                    if self.type == 0:
                        color = (abs(self.map[i][j][0]*255),abs(self.map[i][j][1]*255),abs(self.map[i][j][2]*255))
                    elif self.type == 1:
                        color = (abs((self.map[i][j])*255),125,125)
                    elif self.type == 2:
                        color = (125,abs((self.map[i][j])*255),125)
                    elif self.type == 3:
                        color = (125,125,abs((self.map[i][j])*255))
                    r = pygame.Rect(pos,(self.largeurBloc,self.hauteurBloc))
                    pygame.draw.rect(self.surface,color,r)
                        # pygame.draw.circle(self.surface,color,pos,radius)
        
        if self.grid:
            for obj in self.gridLines:
                obj.draw()
        
        # print()
        # print()
        # print()
        # print()
        
        self.parent.surface.blit(self.surface,self.position.getCoordonnees())