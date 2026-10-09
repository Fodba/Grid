import pygame, random as r
from particule import Particule, COULEURS
from fenetre import Window
from vecteur import Vecteur


# COULEURS = ['red','blue','green']


class Programme:
    def __init__(self) -> None:
        self.nbreParticules = 150
        # self.nbreCouleurs = len(COULEURS)
        self.nbreCouleurs = 1
        self.colorStep = 255 /self.nbreCouleurs
        self.pasDeTemps = .05
        print(self.colorStep)
        self.nbreDimensions = 2
        self.fps = 10
        self.envSize = [400,400]
        self.window = Window(self,self.envSize)
        self.setParametres()
        self.init()
        
    def setParametres(self):
        self.setAttractions()
        self.setDistances()
        self.setRayons()
        
        print(self.attractions)
        print(self.distances)
        print(self.rayons)
        
    def init(self):
        
        self.objets = []
        self.initParticules()
        
        print(self.attractions)
        print(self.distances)
        print(self.rayons)
    
    def setAttractions(self):
        self.attractions = [] # Matrice des forces d'attractions
        for i in range(self.nbreCouleurs):
            self.attractions.append([])
            for j in range(self.nbreCouleurs):
                f = r.uniform(5,10)
                if r.randint(0,100) < 50:
                    f = -f
                self.attractions[i].append(f)
    
    def setDistances(self):
        self.distances = [] # Matrice des distances minimal d'attraction
        for i in range(self.nbreCouleurs):
            self.distances.append([])
            for j in range(self.nbreCouleurs):
                # f = r.randint(5,int(self.envSize[0]/5))
                f = r.randint(1,40)
                self.distances[i].append(f)
    
    def setRayons(self):
        self.rayons = [] # Matrice des rayons maximum d'attraction
        for i in range(self.nbreCouleurs):
            self.rayons.append([])
            for j in range(self.nbreCouleurs):
                f = r.randint(40,self.envSize[0]/4)
                # f = r.randint(self.distances[i][j],self.distances[i][j]*3)
                self.rayons[i].append(f)
    
    def initParticules(self):
        self.objets = []
        for i in range(self.nbreParticules):
            particule = Particule(self.window)
            x,y = [r.uniform(0,x) for x in self.envSize]
            particule.setPosition(x,y)
            x,y = [r.uniform(-1,1) for _ in range(self.nbreDimensions)]
            particule.setVelocite(x,y)
            particule.setVelocite(0,0)
            # couleur = r.randint(0,self.nbreCouleurs-1)
            if i < self.nbreCouleurs:
                particule.type = i
            else:
                particule.type = i % self.nbreCouleurs
            # particule.type = couleur
            # print(couleur)
            particule.setColor(self.colorStep)
            self.objets.append(particule)
    
    def run(self):
        for obj in self.objets:
            obj.update(self.objets,self.attractions,self.distances,self.rayons)
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
        self.window.draw()




