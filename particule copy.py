from classes.vecteur import Vecteur
import pygame

COULEURS = ['red','blue','green']

class Particule:
    def __init__(self,parent) -> None:
        self.parent = parent
        self.position = []
        self.velocite = Vecteur()
        # self.acceleration = Vecteur()
        self.color = "red"
        self.type = 0
        self.forceFactor = 1
        self.masse = 1
        pass

    def setPosition(self,x,y):
        self.position = [x,y]

    def setVelocite(self,x,y):
        self.velocite = Vecteur(valeurs=[x,y])
    
    def setColor(self,valeur):
        # self.type = valeur
        # val = (self.type+1) * valeur
        # val2 = 200-((self.type+1) * valeur)
        # val2 = 150
        # val3 = 150
        if self.type < 3:
            if self.type == 0:
                self.color = (255,0,0)
            elif self.type == 1:
                self.color = (0,255,0)
            elif self.type == 2:
                self.color = (0,0,255)
        else:
            v = self.type % 3
            if v == 0:
                self.color = (255,(self.type * valeur),0)
            elif v == 1:
                self.color = (0,255,(self.type * valeur))
            elif v == 2:
                self.color = ((self.type * valeur),0,255)
        # print(val)
        # self.color = (val,val2,val3)
        # print(self.color)
    
    def getRange(self,valeur,max):
        return ((valeur * 100) / max)/100
    
    def update(self,particules,forces,distances,rayons):
        direction = Vecteur()
        forceTotale = [0,0]
        acceleration = [0,0]
        dis = 0.0
        for particule in particules:
            if particule != self:
                direction = Vecteur(valeurs=particule.position)
                direction -= self.position
                if direction.v[0] >= .5 * self.parent.envSize[0]:
                    direction.v[0] -= self.parent.envSize[0]
                if direction.v[0] <= -(.5 * self.parent.envSize[0]):
                    direction.v[0] += self.parent.envSize[0]
                    
                if direction.v[1] >= .5 * self.parent.envSize[1]:
                    direction.v[1] -= self.parent.envSize[1]
                if direction.v[1] <= -(.5 * self.parent.envSize[1]):
                    direction.v[1] += self.parent.envSize[1]
                # if dis < self.parent.envSize[0] / 2:
                dis = direction.getLength()
                direction = direction.getUnitVecteur()
                if dis < distances[self.type][particule.type]:
                    force = direction.getCoordonnees()
                    force[0] *= forces[self.type][particule.type] * -1.5
                    force[1] *= forces[self.type][particule.type] * -1.5
                    f = self.getRange(dis,distances[self.type][particule.type])
                    # print(f)
                    force[0] *= f
                    force[1] *= f
                    force[0] *= self.forceFactor
                    force[1] *= self.forceFactor
                    forceTotale[0] += force[0]
                    forceTotale[1] += force[1]
                if dis < rayons[self.type][particule.type]:
                    force = direction.getCoordonnees()
                    force[0] *= forces[self.type][particule.type] 
                    force[1] *= forces[self.type][particule.type] 
                    f = self.getRange(dis,rayons[self.type][particule.type])
                    # print(f)
                    force[0] *= f
                    force[1] *= f
                    force[0] *= self.forceFactor
                    force[1] *= self.forceFactor
                    forceTotale[0] += force[0]
                    forceTotale[1] += force[1]
                    # print(forceTotale)
        acceleration[0] += forceTotale[0] / self.masse
        acceleration[1] += forceTotale[1] / self.masse
        self.velocite = acceleration
        # print(self.velocite)
        
    def updatePosition(self,temps):
        self.position[0] += self.velocite[0] * temps
        self.position[1] += self.velocite[1] * temps
        
        self.position[0] = (self.position[0] + self.parent.envSize[0])%self.parent.envSize[0]
        self.position[1] = (self.position[1] + self.parent.envSize[1])%self.parent.envSize[1]
        # print(self.position)
        # print()

    def draw(self) -> None:
        pygame.draw.circle(self.parent.surface,self.color,self.position[:2],3)