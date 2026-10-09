from graphics.fenetre import Window
from graphics.bouton import Bouton
from graphics.grille import Grille
import pygame, random as r,math, json
from datetime import datetime as dt

class Programme:
    def __init__(self) -> None:
        self.fps = 10
        self.go = False
        self.aleatoire = True
        self.setZone(1)
        # self.zone = [-1,1]
        self.voisinnageOmbre = 1
        self.nombreVoisins = [3,4]
        self.voisinMin = 3
        self.voisinMax = 4
        self.voisinNaissance = [3]
        
        # self.zone2 = [-range[index][0],range[index][0]]
        # self.etendue = range[index][1]
        self.tailleGrille = 100
        self.pourcentage = r.randint(15,35)
        self.pourcentage = 25
        self.initMap(self.tailleGrille)
        # self.load()
        self.setColors(self.tailleGrille)
        self.window = Window(self,(1030,830))
        
        self.initProg()
                                
    def setZone(self,index):
        range = [[1,8],[2,24],[3,38],[4,96],[5,192]]
        self.zone = [-range[index][0],range[index][0]]
        self.etendue = range[index][1]
        
    def initMap(self,tailleGrille=20):
        # tailleGrille = 20
        self.map = []
        self.temps = []
        for i in range(tailleGrille):
            self.map.append([])
            self.temps.append([])
            for j in range(tailleGrille):
                if self.aleatoire:
                    # if (i >= (tailleGrille / 10) * 4 and i < (tailleGrille / 10) * 6) and (j >= (tailleGrille / 10) * 4 and j < (tailleGrille / 10) * 6):
                        if r.randint(0,100) <= self.pourcentage:
                            self.map[i].append(0)
                            # self.temps[i].append(0)
                        else:
                            self.map[i].append(1)
                            # self.temps[i].append(1)
                    # else:
                    #     self.map[i].append(1)
                    # self.temps[i].append(1)
                else:
                    self.map[i].append(1)

        
    def init(self,grille):
        self.map = grille
        self.grille.setMap(self.map,self.temps)
        
    def initProg(self):
        self.drawObjets = []
        textes = ["LANCER","STOP","RESET","LOAD","SAVE"]
        
        for i,texte in enumerate(textes):
            b = Bouton(self.window,100,40,texte)
            b.setPosition([75,((i+1)*45) + 5])
            
            self.drawObjets.append(b)
        
        self.grille = Grille(self.window,800,800,self.map,self.temps)
        self.grille.setPosition([220,5])
        self.drawObjets.append(self.grille)
        self.focus = self.grille
        self.grille.setMap(self.map,self.temps)
        
        # self.checkboxNaissance = Checkboxs(self.window,[105,410],"Naissance")
        # self.drawObjets.append(self.checkboxNaissance)
        # self.checkboxSurvie = Checkboxs(self.window,[105,470],"Survie")
        # self.drawObjets.append(self.checkboxSurvie)
        
        # self.sliderTaille = Slider(self.window,[75,285],"Taille")
        # self.drawObjets.append(self.sliderTaille)
        # self.sliderVitesse = Slider(self.window,[75,350],"Vitesse")
        # self.drawObjets.append(self.sliderVitesse)
    
    def reset(self):
        # self.go = False
        # self.initMap(self.tailleGrille)
        if self.aleatoire:
            self.initMap(self.tailleGrille)
        else:
            self.load()
        self.setColors(self.tailleGrille)
        self.init(self.map)
        
    # def save(self):
        
    def save(self,file="cell.json"):
        date = dt.now().isoformat()
        # data = self.cerveau.getData()
        fichier = "maps/map_{}.json".format(date)
        f = open(fichier,"w")
        carte = json.dumps(self.map,indent=4)
        f.write(carte)
        f.close()
    
    def load(self,file="maps/map_ruches2.json"):
        f = open(file, "r")
        self.map = json.load(f)
        # print(data)

    
    def setColors(self,tailleGrille=20):
        self.temps = []
        for i in range(tailleGrille):
            self.temps.append([])
            for j in range(tailleGrille):
                self.setZone(0)
                voisins = self.checkVoisinnage([i,j],self.map)
                self.setZone(self.voisinnageOmbre)
                voisins2 = self.checkVoisinnage([i,j],self.map)
                self.temps[i].append(self.cellColor(i,j,voisins,voisins2))
        
    def cellColor(self,i,j,voisins,voisins2):
        if self.map[i][j] == 0:
            if voisins in self.nombreVoisins:# >= self.voisinMin and voisins <= self.voisinMax:
                return  0 #voisins / 8
            else:
                return 1 - (voisins2 / self.etendue)
        else:
            if voisins in self.voisinNaissance:
                return  0 #voisins / 8
            else:
                return 1 - (voisins2 / self.etendue)
                    
    def updateCell(self,i,j,voisins):
        if self.map[i][j] == 0:
            if voisins in self.nombreVoisins: #>= self.voisinMin and voisins <= self.voisinMax:
                return 0
            else:
                return 1
        else:
            if voisins in self.voisinNaissance:
                return 0
            else:
                return 1
        
    def checkVoisin(self,index,carte):
        compteur = 0
        val = 0
        colonnes = len(carte)
        lignes = len(carte[index[1]])
        s = ""
        for valX in range(self.zone[0],self.zone[1]+1):
            for valY in range(self.zone[0],self.zone[1]+1):
                if valX != index[0] and valY != index[1]:
                    x = index[0] + valX
                    if x < 0:
                        x = colonnes - 1
                    if x == colonnes:
                        x = 0
                    
                    y = index[1] + valY
                    if y < 0:
                        y = lignes - 1
                    if y == lignes:
                        y = 0
                    
                    if carte[x][y] == 0:
                        val += carte[x][y]
                        compteur += 1
        return compteur
    
    def checkVoisinnage(self,index,carte):
        compteur = 0
        colonnes = len(carte)
        lignes = len(carte[index[1]])
        s = ""
        for valX in range(self.zone[0],self.zone[1]+1):
            for valY in range(self.zone[0],self.zone[1]+1):
                # print(valX)
                # print(valY)
                # if valX != 0 and valY != 0:
                # if valX != index[0] and valY != index[1]:
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
                    
                    if carte[x][y] == 0:
                        compteur += 1
        return compteur
        
    def step(self):
        newMap = []
        for i,col in enumerate(self.map):
            newMap.append([])
            for j,line in enumerate(col):
                self.setZone(0)
                voisins = self.checkVoisinnage([i,j],self.map)
                self.setZone(self.voisinnageOmbre)
                voisins2 = self.checkVoisinnage([i,j],self.map)
                newMap[i].append(self.updateCell(i,j,voisins))
                self.temps[i][j] = self.cellColor(i,j,voisins,voisins2)
        self.grille.setMap(newMap,self.temps)
        self.map = newMap
        
        
    
    def addCell(self,position):
        posi = [position[0]-self.grille.position.v[0],position[1]-self.grille.position.v[1]]
        px,py = [math.floor((posi[0] / self.grille.width) * len(self.map)),math.floor((posi[1] / self.grille.height) * len(self.map[0]))]
        
        # print((px,py))
        self.setZone(0)
        voisins = self.checkVoisinnage([px,py],self.map)
        self.setZone(self.voisinnageOmbre)
        voisins2 = self.checkVoisinnage([px,py],self.map)
        
        self.map[px][py] = 0 if self.map[px][py] == 1 else 1
        self.temps[px][py] = 0 if self.map[px][py] == 0 else self.cellColor(px,py,voisins,voisins2)
        self.grille.setMap(self.map,self.temps)
        
        
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
                if obj.nom == "grille":
                    self.addCell(position)
                # print(obj.nom)
                
    def run(self):
        if self.go:
            self.step()

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

    
        
    def draw(self):
        self.window.draw()