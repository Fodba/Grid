import pygame

WIDTH = 900
HEIGHT = 900


class Window():
    def __init__(self,parent,envSize:list=[WIDTH,HEIGHT]) -> None:
        self.parent = parent
        self.envSize = envSize
        self.surface = pygame.display.set_mode(self.envSize)
        self.backColor = (150,50,250)
        self.init()
        
        
    
    def init(self):
        self.objets = []
        self.boutons = []

    def draw(self,part=None) -> None:
        self.surface.fill(self.backColor)
        for obj in self.parent.drawObjets:
            obj.draw()
        # for obj in self.objets:
        #     obj.draw()
        # for obj in self.boutons:
        #     obj.draw()
        if part is None:
            pygame.draw.rect(self.surface,(50,50,255),self.parent.focus.rect,3)
        else:
            pygame.draw.rect(self.surface,(50,50,255),(0,0,0,0),3)
        pygame.display.update()


if __name__ == "__main__":
    window = Window()
    # window.setup()
    window.run()