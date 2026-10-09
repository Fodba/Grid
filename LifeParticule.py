import pygame, random as r
from graphics.particule import Particule, COULEURS
from graphics.fenetre import Window
from classes.vecteur import Vecteur


COULEURS = ['red','blue','green']


class Programme:
    def __init__(self) -> None:
        self.nbreParticules = 100
        self.nbreCouleurs = len(COULEURS)
        self.nbreCouleurs = 3
        # self.colorStep = 255 
        # /self.nbreCouleurs
        self.pasDeTemps = .001
        self.fps = 10
        self.envSize = [900,900]
        self.window = Window(self,self.envSize)
        self.drawObjets = []
        self.init()
        self.setParametres()
        # self.attractions = [] # Matrice des forces d'attractions
        # self.distances = [] # Matrice des distances minimal d'attraction
        # self.rayons = 200 # Matrice des rayons maximum d'attraction


    def run(self):
        for obj in self.drawObjets:
            obj.update(self.drawObjets,self.attractions,self.distances,self.rayons,self.pasDeTemps)
            obj.updatePosition(self.pasDeTemps)
        pass
        

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
                if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_r):
                    self.init()
                if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE):
                    self.setParametres()
                if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_n):
                    self.setParametres()
                    self.init()
                    
            self.run()
            self.draw()
            
            clock.tick(self.fps)

    
        
    def draw(self):
        self.window.draw("part")



    def init(self):
        
        self.objets = []
        self.initParticules()
        
        # print(self.attractions)
        # print(self.distances)
        # print(self.rayons)
        
    def initParticules(self):
        self.drawObjets = []
        for i in range(self.nbreParticules):
            particule = Particule(self.window)
            x,y = [r.uniform(0,x) for x in self.envSize]
            particule.setPosition(x,y)
            x,y = [r.uniform(-1,1) for _ in range(2)]
            particule.setVelocite(x,y)
            particule.type = r.randint(0,self.nbreCouleurs-1)
            # particule.color = COULEURS[particule.type]
            particule.setColor(particule.type)
            self.drawObjets.append(particule)

        
    def setParametres(self):
        self.setAttractions()
        self.setDistances()
        self.setRayons()
        
        # print(self.attractions)
        # print(self.distances)
        # print(self.rayons)
        pass
    
    def setAttractions(self):
        self.attractions = [] # Matrice des forces d'attractions
        for i in range(self.nbreCouleurs):
            self.attractions.append([])
            for j in range(self.nbreCouleurs):
                f = r.uniform(0.5,1.5)
                n = r.uniform(-5,-
                              3)
                self.attractions[i].append([f,n])
    
    def setDistances(self):
        self.distances = [] # Matrice des forces d'distances
        for i in range(self.nbreCouleurs):
            self.distances.append([])
            for j in range(self.nbreCouleurs):
                f = r.uniform(0.5,1.5)
                # n = r.uniform(-1,-2)
                self.distances[i].append(f)
    
    def setRayons(self):
        self.rayons = [] # Matrice des forces d'rayons
        for i in range(self.nbreCouleurs):
            self.rayons.append([])
            for j in range(self.nbreCouleurs):
                f = r.uniform(0.5,1.5)
                # n = r.uniform(-1,-2)
                self.rayons[i].append(f)