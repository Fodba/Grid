from classes.vecteur import Vecteur
import pygame, math
import random as r

COULEURS = ['red','blue','green']

class Particule:
    def __init__(self,parent) -> None:
        self.parent = parent
        self.position = []
        self.velocite = Vecteur()
        self.setVelocite(r.random(),r.random())
        # self.acceleration = Vecteur()
        self.color = "red"
        self.type = 0
        self.forceFactor = 1
        self.masse = 1
        self.radius = 5
        self.friction = 0.1
        pass


    def setPosition(self,x,y):
        self.position = [x,y]
        
    def setVelocite(self,x,y):
        self.velocite = Vecteur(valeurs=[x,y])
    
    def setColor(self,valeur):
        # self.color = (0,0,255)
        if self.type < 3:
            if self.type == 0:
                self.color = (255,0,0)
            elif self.type == 1:
                self.color = (0,255,0)
            elif self.type == 2:
                self.color = (0,0,255)
        
    def update(self,particules,forces,distances,rayons,pasDeTemps):
        direction = Vecteur()
        forceTotale = [0,0]
        acceleration = [0,0]
        dis = 0.0
        for particule in particules:
            if particule != self:
                direction = Vecteur(valeurs=particule.position)
                pos = Vecteur(valeurs=self.position)
                
                direction -= pos
                # if direction.v[0] >= .5 * self.parent.envSize[0]:
                #     direction.v[0] -= self.parent.envSize[0]
                # if direction.v[0] <= -(.5 * self.parent.envSize[0]):
                #     direction.v[0] += self.parent.envSize[0]
                    
                # if direction.v[1] >= .5 * self.parent.envSize[1]:
                #     direction.v[1] -= self.parent.envSize[1]
                # if direction.v[1] <= -(.5 * self.parent.envSize[1]):
                #     direction.v[1] += self.parent.envSize[1]
                # direction -= self.position
                distance = direction.getLength()
                # print(distance)
                # if distance < self.parent.envSize[0] / 3:
                #     force = pos.getDirection(direction)
                #     # force.getUnitVecteur()
                #     forceTotale[0] += force.v[0]
                #     forceTotale[1] += force.v[1]
                # # elif distance <= rayons:
                # else:
                if True:
                    # print("plus grand")
                    force = direction.getDirection(pos)
                    # force.getUnitVecteur()
                    attraction = forces[self.type][particule.type]
                    dis = distances[self.type][particule.type]
                    ray = rayons[self.type][particule.type]
                    f = self.getForces(distance,attraction,dis,ray)
                    # print('**************')
                    # print(forces)
                    # print(attraction)
                    print(distance)
                    # print(force)
                    # print(f)
                    # print(force)
                    # print('**************')
                    force *= f
                # elif distance <= self.radius * 3:
                #     force *= -1
                # force *= pasDeTemps
                    forceTotale[0] += force.v[0]
                    forceTotale[1] += force.v[1]
        
        acceleration[0] += forceTotale[0] * pasDeTemps
        acceleration[1] += forceTotale[1] * pasDeTemps
        self.velocite = acceleration
        # print('**************')
        # print(forceTotale)
        # print(self.velocite)
        # print('**************')
        
        
    def getForces(self,distance,attraction,distances,rayon):
        result = self.getForce(distance,attraction,distances,rayon) + self.getRépulsion(distance,attraction,distances,rayon)
        return result
    
    def getForce(self,distance,attraction,distances,rayon):
        a = rayon
        b = 0.97
        c = 10.8
        d = 0
        e = distances
        j = attraction[0]
        # if attraction[1]: j = -j
        # l = attraction[0]
        l = 15000
        n = -35.3
        # distance += n
        m = l / (distance)
        result = j * (c * (a**b) * (m**a) * (b**m))**e + d
        # print("result: {}".format(result))
        return result
    
    def getRépulsion(self,distance,attraction,distances,rayon):
        a = rayon
        b = 0.97
        c = 10.8
        d = 0
        e = distances
        j = -1.1
        j = attraction[1]
        result = j * (c * (a**b) * (distance**a) * (b**distance))**e + d
        # print("result: {}".format(result))
        return result
        
    def updatePosition(self,temps):
        self.position[0] += self.velocite[0] * temps * self.friction
        self.position[1] += self.velocite[1] * temps * self.friction
        
        self.position[0] = (self.position[0] + self.parent.envSize[0])%self.parent.envSize[0]
        self.position[1] = (self.position[1] + self.parent.envSize[1])%self.parent.envSize[1]
        # print(self.position)
        # print()

    def draw(self) -> None:
        pygame.draw.circle(self.parent.surface,self.color,self.position[:2],self.radius)