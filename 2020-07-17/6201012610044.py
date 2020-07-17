#6201010610044
#this code used for Assignment II

#reference source
#http://archive.petercollingridge.co.uk/book/export/html/6
#http://www.geometrian.com/programming/projects/index.php?project=Circle%20Collisions

import pygame, random, math
pygame.init()
pygame.display.set_caption("Assignment II")
clock = pygame.time.Clock()
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
class myGame():
    ball_obj = []
    size_list = []
    class ball():
        def __init__(self):
            self.red = None; self.green = None; self.blue = None
            self.size = None
            self.x = None; self.y = None
            self.speedx = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
            self.speedy = random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        def _layPosition(self):
            self.red = random.randint(0, 255); self.green = random.randint(0, 255); self.blue = random.randint(0, 255)
            while self.red <= 20 and self.green <= 20 and self.blue <= 20:
                self.red = random.randint(0, 255); self.green = random.randint(0, 255); self.blue = random.randint(0, 255)
            self.size = random.randint(10,20)
            # self.size = random.randint(100,101)
            self.x = random.randint(self.size,scr_w-self.size); self.y = random.randint(self.size,scr_h-self.size)
            if self._checkSamePos() == False:
                myGame.size_list.append(self.size)
                myGame.ball_obj.append(self)
            else:
                try:
                    self._layPosition()
                except RuntimeError:
                    raise ("CAN NOT FIND ROOM TO PLACE!!!")
        def _checkSamePos(self):
            if myGame.ball_obj != []:
                for another_ball in myGame.ball_obj:
                    dist = int(math.hypot(another_ball.x - self.x, another_ball.y - self.y))
                    if (dist < int(another_ball.size + self.size)):

                        return True
                return False
            else:
                return False
        def clearBall(self):
            self.red = None; self.green = None; self.blue = None
            self.size = None
            self.x = None; self.y = None
            self.speedx = None
            self.speedy = None

    def createCircle(self,circle_num):
        for i in range(circle_num):
            self.ball()._layPosition()
            self.size_list.sort()
    def drawCircle(self):
        for circle_obj in self.ball_obj:
            color = (circle_obj.red, circle_obj.green, circle_obj.blue)
            position = (int(circle_obj.x), int(circle_obj.y))
            pygame.draw.circle(screen, color, position, circle_obj.size)
    def isInCircle(self,x,y):
        for ball in self.ball_obj:
            if ((x - ball.x) * (x - ball.x) + (y - ball.y) * (y - ball.y) <= ball.size**2):
                print(ball.x,ball.y,self.isBiggest(ball))
                return ball
        return None
    def isBiggest(self,ball):
        max_num = max(self.size_list)
        if ball == None:
            return False
        else:
            if ball.size == max_num:
                return True
            else:
                return False
    def deleteBall(self,ball):
        pygame.draw.circle(screen, (0, 0, 0), (int(ball.x), int(ball.y)), ball.size)
        self.size_list.pop()
        self.ball_obj.remove(ball)
        ball.clearBall()

    def move(self):
        for ball in self.ball_obj:
            ball.x += ball.speedx
            ball.y += ball.speedy
    def impact(self):
        for ball in self.ball_obj:
            if ball.x < ball.size or ball.x > scr_w-ball.size:    ball.speedx *= -1
            if ball.y < ball.size or ball.y > scr_h-ball.size:    ball.speedy *= -1
            for ball in self.ball_obj:
                for ball2 in self.ball_obj:
                    if ball != ball2:
                        if math.sqrt(  ((ball.x-ball2.x)**2)  +  ((ball.y-ball2.y)**2)  ) <= (ball.size+ball2.size):
                            self.CircleCollide(ball,ball2)

    def CircleCollide(self,C1,C2):
        C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
        XDiff = -(C1.x-C2.x)
        YDiff = -(C1.y-C2.y)
        XSpeed = 0
        YSpeed = 0
        Angle = 0.5*math.pi + math.atan2(YDiff, XDiff)
        if XDiff > 0:
            if YDiff > 0:
                Angle = math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -C1Speed*math.cos(math.radians(Angle))
                YSpeed = -C1Speed*math.sin(math.radians(Angle))
            elif YDiff < 0:
                Angle = math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -C1Speed*math.cos(math.radians(Angle))
                YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif XDiff < 0:
            if YDiff > 0:
                Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -C1Speed*math.cos(math.radians(Angle))
                YSpeed = -C1Speed*math.sin(math.radians(Angle))
            elif YDiff < 0:
                Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
                XSpeed = -C1Speed*math.cos(math.radians(Angle))
                YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif XDiff == 0:
            if YDiff > 0:
                Angle = -90
            else:
                Angle = 90
            XSpeed = C1Speed*math.cos(math.radians(Angle))
            YSpeed = C1Speed*math.sin(math.radians(Angle))
        elif YDiff == 0:
            if XDiff < 0:
                Angle = 0
            else:
                Angle = 180
            XSpeed = C1Speed*math.cos(math.radians(Angle))
            YSpeed = C1Speed*math.sin(math.radians(Angle))
        C1.speedx = XSpeed
        C1.speedy = YSpeed
                
game = myGame()
game.createCircle(20)
game.drawCircle()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(game.size_list) == 0:
                print("End game")
            else:
                mouse_pos = pygame.mouse.get_pos()
                ball = game.isInCircle(mouse_pos[0],mouse_pos[1])
                if game.isBiggest(ball):
                    game.deleteBall(ball)
    game.move()
    game.impact()
    screen.fill((0,0,0))
    game.drawCircle()
    pygame.display.flip()
pygame.quit()

