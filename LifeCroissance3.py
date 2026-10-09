from graphics.fenetre import Window
from graphics.bouton import Bouton
from graphics.grille2 import Grille as GrilleU
from graphics.grille3 import Grille
import pygame, random as r,math, json
from datetime import datetime as dt

class Programme:
    def __init__(self) -> None:
        self.fps = 5
        self.go = False
        
        self.tailleGrille = 50
        self.pourcentage = r.randint(15,35)
        self.pourcentage = 25
        self.initMap(self.tailleGrille)
        self.window = Window(self,(1130,880))
        
        self.initProg()
        
    def initMap(self,tailleGrille=20):
        self.map = []
        self.mapA = []
        self.mapB = []
        self.mapC = []
        self.temps = []
        for i in range(tailleGrille):
            self.map.append([])
            self.mapA.append([])
            self.mapB.append([])
            self.mapC.append([])
            self.temps.append([])
            for j in range(tailleGrille):
                a = r.random()
                b = r.random()
                c = r.random()
                self.map[i].append([a,b,c])
                self.mapA[i].append(a)
                self.mapB[i].append(b)
                self.mapC[i].append(c)
        
        # print(self.map)
                                
    # def init(self,grille):
    #     self.map = grille
    #     self.grille.setMap(self.map)
        
        
        
    def initProg(self):
        self.drawObjets = []
        textes = ["LANCER","STOP","RESET","LOAD","SAVE"]
        
        for i,texte in enumerate(textes):
            b = Bouton(self.window,100,40,texte)
            b.setPosition([75,((i+1)*45) + 5])
            
            self.drawObjets.append(b)
        
        self.grille = Grille(self.window,400,400,self.map)
        self.grille.setPosition([220,20])
        self.drawObjets.append(self.grille)
        self.focus = self.grille
        self.grille.setMap(self.map)
        
        self.grilleA = Grille(self.window,400,400,self.mapA,1)
        self.grilleA.setPosition([650,20])
        self.drawObjets.append(self.grilleA)
        self.focus = self.grilleA
        self.grilleA.setMap(self.mapA)
        
        self.grilleB = Grille(self.window,400,400,self.mapB,2)
        self.grilleB.setPosition([220,465])
        self.drawObjets.append(self.grilleB)
        self.focus = self.grilleB
        self.grilleB.setMap(self.mapB)
        
        self.grilleC = Grille(self.window,400,400,self.mapC,3)
        self.grilleC.setPosition([650,465])
        self.drawObjets.append(self.grilleC)
        self.focus = self.grilleC
        self.grilleC.setMap(self.mapC)
        
        
    def loop(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT
                    or (event.type == pygame.KEYDOWN
                    and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q))
                ):
                    run = False
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_r):
                    self.reset()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_s):
                    self.save()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_a):
                    if self.aleatoire:
                        self.aleatoire = False
                    else:
                        self.aleatoire = True
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_n):
                    self.step()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkSouris(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_g):
                    if self.grille.grid:
                        self.grille.grid = False
                    else:
                        self.grille.grid = True
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
                    if self.go:
                        self.go = False
                    else:
                        self.go = True
            
            # self.init()
            self.run()
            self.draw()
            
            clock.tick(self.fps)
            
    def run(self):
        if self.go:
            self.step()
        
    def draw(self):
        self.window.draw()
        
    def checkSouris(self,position):
        r = pygame.Rect(position,(1,1))
        for obj in self.drawObjets:
            if obj.rect.colliderect(r):
                self.focus = obj
                if obj.nom == "RESET":
                    self.reset()
                if obj.nom == "LANCER":
                    self.go = True
                if obj.nom == "STOP":
                    self.go = False
                if obj.nom == "SAVE":
                    self.save()
                # if obj.nom == "grille":
                #     self.addCell(position)
                # print(obj.nom)

    def getCroissanceA(self,x):
        a = math.sin(7*(x-.33)*(x-.33))
        return (((a*a) - .5) * 2) + .006
    
    def getCroissanceB(self,x):
        a = 5.6
        b = 9.4
        c = -1.5
        result = val1 = b * x - math.exp(x) * a * x*x + c
        print(result)
        print(x)
        return result
    
    def getCroissanceC(self,x):
        a = 1.64
        b = 4.5
        c = -1.2
        result = (a*math.cos(x)+c*x)*(b*math.sin(x)+c)
        # print(result)
        # print(x)
        return result

    def step(self):
        newMap = []
        newMapA = []
        newMapB = []
        newMapC = []
        for i,col in enumerate(self.map):
            newMap.append([])
            newMapA.append([])
            newMapB.append([])
            newMapC.append([])
            for j, line in enumerate(col):
                voisins = self.checkVoisin([i,j],self.map)
                newVals = self.updateCell(i,j,voisins)
                newMap[i].append(newVals)
                newMapA[i].append(newVals[0])
                newMapB[i].append(newVals[1])
                newMapC[i].append(newVals[2])
        self.grille.setMap(newMap)
        self.map = newMap
        self.grilleA.setMap(newMapA)
        self.mapA = newMapA
        self.grilleB.setMap(newMapB)
        self.mapB = newMapB
        self.grilleC.setMap(newMapC)
        self.mapC = newMapC
        
    def updateCell(self,i,j,voisins):
        val = []
        vA,vB,vC = self.getCroissanceA(voisins[0]),self.getCroissanceA(voisins[1]),self.getCroissanceA(voisins[2])
        if vA >= 1: vA = 1
        if vA <= 0: vA = 0
        if vB >= 1: vB = 1
        if vB <= 0: vB = 0
        if vC >= 1: vC = 1
        if vC <= 0: vC = 0
        val.append(vA)
        val.append(vB)
        val.append(vC)
        # for l,x in enumerate(self.map[i][j]):
        #     # print("--------------------------------------------------")
        #     # print(self.map[i][j])
        #     # print(i)
        #     # print(j)
        #     # print(l)
        #     # print(x)
        #     # print(voisins)
        #     # print("--------------------------------------------------")
        #     v = self.getCroissanceC(voisins[l])
        #     print(v)
        #     if v >= 1: v = 1
        #     if v <= -1: v = -1
        #     val.append(v)
        # print(val)
        # print("****************************")
        return val
        
            
    def checkVoisin(self,index,carte):
        compteur = 0
        val = []
        colonnes = len(carte)
        lignes = len(carte[index[1]])
        zone = [-1,1]
        for valX in zone:
            for valY in zone:
                x = index[0] + valX
                if x < 0:
                    x = colonnes + x
                if x >= colonnes:
                    x = x - colonnes 
                
                y = index[1] + valY
                if y < 0:
                    y = lignes + y
                if y >= lignes:
                    y = y - lignes 
                
                for k in carte[x][y]:
                        compteur += k
                val.append(compteur)
        # print(val)
        return val