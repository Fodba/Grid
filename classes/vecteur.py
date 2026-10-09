
# DONE

# Notation
# Addition
# Soustraction
# longueur du vecteur
# copie du vecteur
# normalisation
# Mutliplication Scalaire
# Division Scalaire
# operateur de comparaison ( < > == )
# Mutliplication des composants
# Division des composants
# Produit scalaire (dotProduct)


# TODO
# produit scalaire V2
# produit en croix

import math, random as r


class Vecteur():
    def __init__(self,dimensions=2,valeurs=None) -> None:
        self.dimensions = abs(dimensions)
        if valeurs is not None:
            # for i in range(self.getDimensions()):
            #     self.v.append(valeurs[i])
            self.v = valeurs
            
            if type(valeurs)==(Vecteur):
                    self.v = valeurs.getVecteur()
            elif type(valeurs)==(list):
                for i in range(len(valeurs)):
                    self.v[i] = valeurs[i]
        else:
            self.initVecteur()
        self.precision = 2
    
    def initVecteur(self):
        self.v = []
        for i in range(self.getDimensions()):
            self.v.append(0)
    
    def initRandomVecteur(self,min,max):
        self.v = []
        for i in range(self.getDimensions()):
            self.v.append(r.randint(min,max))
        
    def setPrecision(self,precision: int):
        self.precision = precision
    
    def getDimensions(self):
        return self.dimensions
    
    def getCoordonnees(self):
        coordonnes = []
        for coord in self.v:
            coordonnes.append(coord)
        return coordonnes
    
    def __add__(self,o):
        vec = Vecteur(dimensions=self.getDimensions())
        vec.setPrecision(self.precision)
        if type(o)==(Vecteur):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] + o.v[i]
            return vec
        elif type(o)==(list):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] + o[i]
            return vec
        else:
            raise Exception("Impossible d'additionner avec ce type")
    
    def __sub__(self,o):
        vec = Vecteur(dimensions=self.getDimensions())
        vec.setPrecision(self.precision)
        if type(o) == (int) or type(o) == (float):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] - o
            return vec
        if type(o)==(Vecteur):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] - o.v[i]
            return vec
        elif type(o)==(list):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] - o[i]
            return vec
        else:
            raise Exception("Impossible de soustraire avec ce type")
    
    def __mul__(self,o):
        vec = Vecteur(dimensions=self.getDimensions())
        vec.setPrecision(self.precision)
        if type(o) == (int) or type(o) == (float):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] * o
            return vec
        if type(o)==(Vecteur):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] * o.v[i]
            return vec
        else:
            raise Exception("Impossible de multiplier avec ce type")
    
    def __truediv__(self,o):
        vec = Vecteur(dimensions=self.getDimensions())
        vec.setPrecision(self.precision)
        if type(o) == (int) or type(o) == (float) and o != 0:
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] / o
            return vec
        if type(o)==(Vecteur):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] / o.v[i]
            return vec
        else:
            raise Exception("Impossible de diviser avec ce type")
    
    def __floordiv__(self,o):
        vec = Vecteur(dimensions=self.getDimensions())
        vec.setPrecision(self.precision)
        if type(o) == (int) or type(o) == (float) and o != 0:
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] / o
            return vec
        if type(o)==(Vecteur):
            for i in range(self.getDimensions()):
                vec.v[i] = self.v[i] / o.v[i]
            return vec
        else:
            raise Exception("Impossible de diviser avec ce type")
    
    def __lt__(self,o):
        if type(o) == (Vecteur):
            ol = o.getLength()
            l = self.getLength()
            return l < ol
        else:
            raise Exception("Impossible de comparer avec ce type")
    
    def __le__(self,o):
        if type(o) == (Vecteur):
            ol = o.getLength()
            l = self.getLength()
            return l <= ol
        else:
            raise Exception("Impossible de comparer avec ce type")
    
    def __gt__(self,o):
        if type(o) == (Vecteur):
            ol = o.getLength()
            l = self.getLength()
            return l > ol
        else:
            raise Exception("Impossible de comparer avec ce type")
    
    def __ge__(self,o):
        if type(o) == (Vecteur):
            ol = o.getLength()
            l = self.getLength()
            return l >= ol
        else:
            raise Exception("Impossible de comparer avec ce type")
    
    def __eq__(self,o):
        if type(o) == (Vecteur):
            equal = True
            for i in range(self.getDimensions()):
                if self.v[i] != o.v[i]:
                    equal = False
            return equal
        else:
            raise Exception("Impossible de comparer avec ce type")
    
    def __ne__(self,o):
        if type(o) == (Vecteur):
            equal = True
            for i in range(self.getDimensions()):
                if self.v[i] != o.v[i]:
                    equal = False
            return not equal
        else:
            raise Exception("Impossible de comparer avec ce type")
    
    def getVecteur(self):
        vec = Vecteur(dimensions=self.getDimensions())
        vec.setPrecision(self.precision)
        for i in range(vec.getDimensions()):
            vec.v[i] = self.v[i]
        return vec
    
    def getLength(self):
        sqrLength = 0
        for val in self.v:
            sqrLength += val*val
        length = math.sqrt(sqrLength)
        return length
    
    def reverseVecteur(self):
        v = self.getVecteur()
        for i in range(v.getDimensions()):
            v.v[i] = -self.v[i]
        return v
    
    def getUnitVecteur(self):
        v = None
        v = self.getVecteur()
        v.setPrecision(self.precision)
        l = v.getLength()
        if l != 0:
            for i in range(v.getDimensions()):
                v.v[i] = self.v[i] / l
        return v
    
    def dotProduct(self,Vecteur):
        if type(Vecteur) == (Vecteur):
            vals = []
            for i in range(self.getDimensions()):
                vals.append(self.v[i] * Vecteur.coordonnees[i])
            total = 0
            for i in range(len(vals)):
                total += vals[i]
            return total
        else:
            raise Exception("Impossible d'opérer avec ce type")
    
    def crossProduct(self,Vecteur):
        if type(Vecteur) == (Vecteur):
            vals = [1 for i in range(self.getDimensions())]
            for i in range(self.getDimensions()):
                vals[i] = self.v[i] * Vecteur.coordonnees[i]
            total = 0
            for i in range(len(vals)):
                total += vals[i]
            return total
        else:
            raise Exception("Impossible d'opérer avec ce type")
            
    def getDistance(self,vecteur):
        if type(vecteur) == (Vecteur):
            vals = [1 for i in range(self.getDimensions())]
            for i in range(self.getDimensions()):
                vals[i] = math.pow((self.v[i] - vecteur.v[i]),2)
            total = 0
            for i in range(len(vals)):
                total += vals[i]
            return total ** (1/float(len(vals)))
        else:
            raise Exception("Impossible d'opérer avec ce type")
            
    def getDistanceCarre(self,vecteur):
        if type(vecteur) == (Vecteur):
            vals = [1 for i in range(self.getDimensions())]
            for i in range(self.getDimensions()):
                vals[i] = math.pow((self.v[i] - vecteur.v[i]),2)
            total = 0
            for i in range(len(vals)):
                total += vals[i]
            return total
        else:
            raise Exception("Impossible d'opérer avec ce type")
            
    def getDirection(self,vecteur):
        vals = Vecteur(self.getDimensions())
        if type(vecteur) == (Vecteur):
            # vals = [1 for i in range(self.getDimensions())]
            for i in range(self.getDimensions()):
                vals.v[i] = self.v[i] - vecteur.v[i]
            return vals
        else:
            raise Exception("Impossible d'opérer avec ce type")
        
    
    def __str__(self) -> str:
        s = "Vecteur: ["
        for val in self.v:
            s += "({}), ".format(round(val,self.precision))
        s = s[:-2]
        s += "]"
        return s
            