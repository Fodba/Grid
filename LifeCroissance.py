from graphics.fenetre import Window
from graphics.bouton import Bouton
from graphics.grille2 import Grille
import pygame, random as r,math, json
from datetime import datetime as dt

class Programme:
    def __init__(self) -> None:
        self.dt = 0.1
        self.fps = 30 * self.dt
        self.go = False
        self.rayonInterne = 5
        self.rayon = 4
        
        self.tailleGrille = 50
        self.pourcentage = r.randint(15,35)
        self.pourcentage = 50
        self.initMap(self.tailleGrille)
        self.window = Window(self,(1030,830))
        
        self.initProg()
        
    def initMap(self,tailleGrille=20):
        self.map = []
        self.temps = []
        for i in range(tailleGrille):
            self.map.append([])
            self.temps.append([])
            for j in range(tailleGrille):
                self.map[i].append([r.random(),1,1])
                # self.map[i].append([r.random(),r.random()])
                # self.map[i].append(r.random())
        
        # print(self.map)
                                
    def init(self,grille):
        self.map = grille
        self.grille.setMap(self.map)
        
        
        
    def initProg(self):
        self.drawObjets = []
        textes = ["LANCER","STOP","RESET","LOAD","SAVE"]
        
        for i,texte in enumerate(textes):
            b = Bouton(self.window,100,40,texte)
            b.setPosition([75,((i+1)*45) + 5])
            
            self.drawObjets.append(b)
        
        self.grille = Grille(self.window,800,800,self.map)
        self.grille.setPosition([220,5])
        self.drawObjets.append(self.grille)
        self.focus = self.grille
        self.grille.setMap(self.map)
        
        
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
        return (((a*a) - .5) * 2) 
    
    def getCroissanceB(self,x):
        a = 5.6
        b = 11.5
        c = -1.5
        result = (b * x) - (math.exp(x) * a * x*x) + c
        print(result)
        print(x)
        if result >= 1: result = 1
        if result <= -1: result = -1
        return result
    
    def getCroissanceC(self,x):
        a = .59
        b = 3.2
        c = -2.6
        result = (a*math.cos(x)+c*x)*(b*math.sin(x)+c)
        # print(result)
        # print(x)
        return result
    
    def getCroissanceD(self,x):
        a = 1.34
        b = 1.6
        c = .8
        d = 2.1
        # a = 6.9
        # b = 0.1
        # c = 1.4
        # d = 1.4
        result = d*(math.sin((x**c)*a)) - b
        # print(result)
        # print(x)
        return result
    
    def getCroissanceD2(self,x):
        # a = 3.8
        # b = .1
        # c = 1.3
        a = 1.34
        b = 1.6
        c = .8
        d = 2.1
        result = d*(math.sin((x**c)*(c**a))) - b
        # print(result)
        # print(x)
        return result
    
    def getCroissanceE(self,x):
        a = 9.7
        b = .1
        c = 1.1
        result = math.sin((x**c)*(c**a)) - b
        # print(result)
        # print(x)
        return result
    
    def getCroissanceF(self,x):
        a = 2.8
        b = .5
        c = 1
        # a = 2.9
        # b = .5
        # c = .7
        d = 1.3
        result = (d * math.sin((x**c)*a)) - b
        # print(result)
        # print(x)
        return result
    
    def getCroissanceG(self,x):
        a = .96
        b = .2
        c = 6.9
        d = -2.2
        e = 2.7
        j = 0.8
        result = j * (c * (a**b) * (x**a) * (b**x))**e + d
        # print(result) 
        # print(x)
        return result

    def step(self):
        newMap = []
        for i,col in enumerate(self.map):
            newMap.append([])
            for j, line in enumerate(col):
                voisins = self.checkVoisins(self.map,i,j)
                voisins2 = self.checkVoisins2(self.map,i,j)
                valVoisins = self.updateCell(i,j,voisins) #* self.dt
                valVoisins2 = self.updateCell2(i,j,voisins2) #* self.dt
                valVoisins3 = self.updateCell3(i,j,voisins,voisins2) #* self.dt
                # valVoisins +=  valVoisins3
                
                newMap[i].append([valVoisins,valVoisins2,valVoisins3])
                # val = self.updateCell(i,j,voisins)+self.updateCell2(i,j,voisins2)
                # newMap[i].append(val)
        self.grille.setMap(newMap)
        self.map = newMap
        
    def updateCell(self,i,j,voisins):
        # val = self.getCroissanceD(voisins)
        val = self.getCroissanceD(voisins)  + self.map[i][j][0]
        # val = self.getCroissanceD2(voisins)  + self.map[i][j][0]
        # val = self.getCroissanceD2(voisins) 
        if val >= 1: val = 1 
        if val <= 0: val = 0
        return val
        
    def updateCell2(self,i,j,voisins):
        # val = self.getCroissanceD2(voisins)
        val = self.getCroissanceD2(voisins)  + self.map[i][j][1]
        # val = self.getCroissanceD(voisins)  + self.map[i][j][1]
        # val = self.getCroissanceD(voisins) 
        if val >= 1: val = 1 
        if val <= 0: val = 0
        return val
        
    def updateCell3(self,i,j,voisins,voisins2):
        # val = self.getCroissanceD(voisins)  + self.map[i][j]
        val = self.updateCell(i,j,voisins) + self.updateCell2(i,j,voisins2)
        # val = self.updateCell(i,j,voisins) + self.updateCell2(i,j,voisins2)
        if val >= 1: val = 1 
        if val <= 0: val = 0
        return val
        
            
    def checkVoisin(self,index,carte):
        compteur = 0
        val = 0
        colonnes = len(carte)
        lignes = len(carte[index[1]])
        zone = [-2,2]
        for valX in (zone[0],zone[1]):
            for valY in (zone[0],zone[1]):
                if valX == 0 and valY == 0:
                    pass
                else:
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
                    
                    # for k in carte[x][y]:
                    #         compteur += k
                    # val.append(compteur)
                    # print(carte[x][y])
                    v = carte[x][y]
                    # if v >= 1: v = .9
                    # if v <= -1: v = -.9
                    val += v
                    compteur += 1
        # print(val)
        return val / compteur
    
    def checkVoisins(self,matrice,i,j):
        rayon = 2
        val = 0
        compteur = 0
        for di in range(-rayon,rayon+1):
            for dj in range(-rayon,rayon+1):
                ni, nj = i + di, j + dj
                distance = (di**2 + dj**2)**0.5
                ni = (ni + len(matrice)) % len(matrice)
                nj = (nj + len(matrice[0])) % len(matrice[0])
                if distance <= self.rayonInterne:
                    if (ni,nj) != (i,j):
                        # val += matrice[ni][nj]
                        val += matrice[ni][nj][0]
                        compteur += 1
        return val #/ compteur
    
    def checkVoisins2(self,matrice,i,j):
        voisins = []
        val = 0
        compteur = 0
        for di in range(-self.rayon,self.rayon+1):
            for dj in range(-self.rayon,self.rayon+1):
                ni, nj = i + di, j + dj
                distance = (di**2 + dj**2)**0.5
                ni = (ni + len(matrice)) % len(matrice)
                nj = (nj + len(matrice[0])) % len(matrice[0])
                if distance <= self.rayon and distance > self.rayonInterne:
                    if (ni,nj) != (i,j):
                        # val += matrice[ni][nj]
                        val += matrice[ni][nj][0]
                        compteur += 1
        return val #/ compteur