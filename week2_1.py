#6201010610044
#this code used for Assignment I

import pygame, random, math
from operator import itemgetter
import numpy as np
pygame.init()
pygame.display.set_caption("Assignment I")
clock = pygame.time.Clock()
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
temp_pos_x = []
temp_pos_y = []
temp_size = []
ziped = []
count = 0
maxnumber = 0
class myGame():
    class ball():
        def __init__(self):
            self.x = random.randint(0,scr_w); self.y = random.randint(0,scr_h)
            self.size = random.randint(10,20)
            self.red = random.randint(0,255); self.green = random.randint(0,255); self.blue = random.randint(0,255)
            while(self.red == 0 and self.green == 0 and self.blue == 0):# if black
                self.red = random.randint(0,255); self.green = random.randint(0,255); self.blue = random.randint(0,255)

        def getcolor(self):
            return self.red, self.green, self.blue
        def getsize(self):
            return self.size
        def getpos(self):
            return self.x, self.y

    def draw(self,num):
        global count 
        if (count < num):
            draw = True
            myball = self.ball()
            for i in range(len(temp_size)):
                if (len(temp_size)==0):
                    pygame.draw.circle(screen, myball.getcolor(), myball.getpos(), myball.getsize())
                    x,y = myball.getpos()
                    temp_pos_x.append(x); temp_pos_y.append(y); temp_size.append(myball.getsize())
                else:
                    x,y = myball.getpos()
                    dist = int(math.hypot(temp_pos_x[i] - x, temp_pos_y[i] - y))
                    if dist < int(temp_size[i]+myball.getsize()):
                        draw = False
            if draw:
                pygame.draw.circle(screen, myball.getcolor(), myball.getpos(), myball.getsize())
                x,y = myball.getpos()
                temp_pos_x.append(x); temp_pos_y.append(y); temp_size.append(myball.getsize())
                count += 1
        elif count == num:
            count += 1
            ziping = list(zip(temp_pos_x,temp_pos_y,temp_size))
            ziping = sorted(ziping, key=itemgetter(2))
            ziping = list(zip(*ziping))
            ziping = [list(ele) for ele in ziping]
            return ziping
        

def is_circle(circle_x, circle_y, radius, x, y,index): 

    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= radius**2): 

        return(index)

def delete_circle(zippack, index):
    xlist = ziped[0]
    ylist = ziped[1]
    sizelist = ziped[2]
    maxnumber = max(sizelist)
    if maxnumber == sizelist[index]:
        pygame.draw.circle(screen, (0, 0, 0), (xlist[index], ylist[index]), sizelist[index])
        ziped[0].pop(index); ziped[1].pop(index); ziped[2].pop(index)
    
circle_num = 100
flag = False
press_index = None
running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(circle_num):
                try:
                    press_index = is_circle(ziped[0][i], ziped[1][i], ziped[2][i],mouse_pos[0],mouse_pos[1],i)
                    if(press_index != None):
                        delete_circle(ziped,i)
                        break
                except:
                    circle_num - 1
                    break

                    
    game = myGame()
    z = game.draw(circle_num)
    if (z) != None and flag == False:
        ziped = z
        flag = True
    pygame.display.update()
    
pygame.quit()
