from Tree import *
class Draw():
    import pygame
    def __init__(self,equation):
        self.equation = equation
        self.root = Tree(Operator(equation).get()).insert()
        self.high = self.root[0].getHeight()
        self.pygame.init()
        self.scr_w,self.scr_h = 1280,760
        self.screen  = self.pygame.display.set_mode((self.scr_w, self.scr_h))
        self.text_font = self.pygame.font.SysFont("leelawadeeui", 30)
        self.clock = self.pygame.time.Clock()
        self.screen.fill((255,255,255))

        self.is_running = True
    def recursive(self, root, pos, parameter, create_root = False):
        OFFSET_X,OFFSET_Y,RAD = parameter
        x,y = pos
        self.printCircle(pos,RAD,root.isLeaf())
        self.printText(root.data, pos)
        if create_root == False:
            if root.data == '!':
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x, y+OFFSET_Y),1)
                return self.recursive(root.left, (x,y+OFFSET_Y), parameter)
            elif root.left and root.right:
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x-OFFSET_X, y+OFFSET_Y),1)
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x+OFFSET_X, y+OFFSET_Y),1)
                return self.recursive(root.left, (x-OFFSET_X,y+OFFSET_Y), parameter),self.recursive(root.right, (x+OFFSET_X,y+OFFSET_Y), parameter)
            elif root.left:
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x-OFFSET_X, y+OFFSET_Y),1)
                return self.recursive(root.left, (x-OFFSET_X,y+OFFSET_Y), parameter)
            elif root.right:
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x+OFFSET_Y, y+OFFSET_Y),1)
                return self.recursive(root.right, (x+OFFSET_X,y+OFFSET_Y), parameter)
            else:
                pass
    def printText(self,text,pos):
        x,y = pos
        x = int(x);y = int(y)
        text = self.text_font.render(text, True, (0,0,0))
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def printCircle(self,pos,rad,draw_rect = False):
        x,y = pos
        x = int(x);y = int(y)
        if draw_rect == True:
            rect =  self.pygame.draw.circle(self.screen,(255,255,255),(x,y),rad,1)
            self.pygame.draw.rect(self.screen,(0,0,0),rect,1)
        else:
            self.pygame.draw.circle(self.screen,(0,0,0),(x,y),rad,1)
        

    def draw(self):
        OFFSET_X = 80
        OFFSET_Y = 70
        RAD = 20
        OFFSET_2 = 200
        root = self.root[0]
        pos = (self.scr_w/2,20)
        x,y = pos
        child_offset = (self.high-1)*RAD

        parameter = (OFFSET_X, OFFSET_Y, RAD)

        #Crate Root
        self.recursive(root,pos,parameter,True)
        #Create Child
        if root.data == '!':
            self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x, y+OFFSET_Y),1)
            return self.recursive(root.left, (x, y+OFFSET_Y), parameter)
        else:           
            if root.left and root.right:
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x-child_offset-OFFSET_2, y+OFFSET_Y),1)
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x+child_offset+OFFSET_2, y+OFFSET_Y),1)
                return self.recursive(root.left, (x-child_offset-OFFSET_2, y+OFFSET_Y), parameter), self.recursive(root.right, (x+child_offset+OFFSET_2, y+OFFSET_Y), parameter)
            elif root.left:
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x-child_offset-OFFSET_2, y+OFFSET_Y),1)
                return self.recursive(root.left, (x-child_offset-OFFSET_2, y+OFFSET_Y), parameter)
            elif root.right:
                self.pygame.draw.line(self.screen,(0,0,0),(x,y),(x+child_offset+OFFSET_2, y+OFFSET_Y),1)
                return self.recursive(root.right, (x+child_offset+OFFSET_2, y+OFFSET_Y), parameter)
            else:
                pass

    def getPhoto(self):
        self.draw()
        
        text = self.text_font.render(self.equation, True, (0,0,0))
        self.screen.blit(text, (0,self.scr_h-50))
        
        self.pygame.display.update()

        self.pygame.image.save(self.screen, "Python\\Lab_Software\\expression tree logical\\screenshot\\screenshot.jpeg")
        
    def loop(self):
        while self.is_running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.is_running = False
            self.draw()
            self.pygame.display.update()
        pygame.quit()
            
if __name__ == "__main__":
    x = Draw("!(1+0)")
    x.getPhoto()



            


        




    


