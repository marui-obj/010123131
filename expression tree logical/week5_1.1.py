class Stack():
    stack_list = []
    def __str__(self):
        return "{}".format(self.stack_list)
    def push(self,data):
        self.stack_list.append(data)
    def pop(self):
        try:
            return_value = self.stack_list.pop()
            return return_value
        except IndexError:
            raise IndexError("Stack index error")
    def size(self):
        return len(len(self.stack_list))
    def is_empty(self):
        return self.stack_list == []
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[len(self.stack_list)-1]
class Operator():
    def __init__(self,express):
        self.express = express
        self.postfix = []
        self.__to_posfix()
    def __to_posfix(self):
        mystack = Stack()
        prec = {'(':0, '!':1, '&':2, '+':3}
        operator_list = ['(','!','&','+',')']
        tokenList = self.express
        bracket_flag = False
        temp_char = ""
        for token in tokenList:
            if token == " ":
                continue
            if token not in operator_list:
                temp_char += token
            elif token in operator_list:
                if temp_char != "":
                    self.postfix.append(temp_char)
                    temp_char = ""
                    while mystack.peek() == '!':
                        self.postfix.append(mystack.pop())

                if token == '(':
                    if mystack.peek() == '!':
                        bracket_flag = True
                    mystack.push(token)
                elif token == '!':
                    mystack.push(token)
                elif token == ')':
                    topToken = mystack.pop()
                    while topToken != '(':
                        self.postfix.append(topToken)
                        topToken = mystack.pop() 
                    if bracket_flag == True and mystack.peek() == '!':
                        self.postfix.append(mystack.pop())
                        bracket_flag = False
                else:
                    while(not mystack.is_empty()) and \
                        (prec[mystack.peek()] >= prec[token]):
                        self.postfix.append(mystack.pop())
                    mystack.push(token)
        if temp_char != "":
            self.postfix.append(temp_char)
        while not mystack.is_empty():
            self.postfix.append(mystack.pop())
        print(''.join([str(elem) for elem in self.postfix]) )
        print(self.postfix)
    def get(self):
        return self.postfix      
class Tree():
    class Node():
        def __init__(self,data):
            self.left = None
            self.right = None
            self.data = data
        def getHeight(self):
            if self.left and self.right:
                return 1 + max(self.left.getHeight(),self.right.getHeight())
            elif self.left:
                return 1 + self.left.getHeight()
            elif self.right:
                return 1 + self.right.getHeight()
            else :
                return 1
        def isLeaf(self):
            if self.left == None and self.right == None:
                return True
            return False
        def isNot(self):
            if self.data == '!':
                return True
            return False
    def __init__(self,postfix_list):
        self.postfix_list = postfix_list
        self.root = None
    def insert(self):
        operator_list = ['&','+']
        postfix = self.postfix_list
        mystack = Stack()
        for var in postfix:
            if var in operator_list:
                operator_node = self.Node(var)
                operator_node.right = mystack.pop()
                operator_node.left = mystack.pop()
                mystack.push(operator_node) 
            elif var == '!':
                operator_node = self.Node(var)
                operator_node.left = mystack.pop()
                mystack.push(operator_node)
            else:
                mystack.push(self.Node(var))
        self.root = mystack.stack_list
        return mystack.stack_list
class Draw():
    import pygame
    def __init__(self,equation):
        self.equation = equation
        self.root = Tree(Operator(equation).get()).insert()
        self.high = self.root[0].getHeight()
        self.pygame.init()
        self.scr_w,self.scr_h = 1500,960
        self.screen  = self.pygame.display.set_mode((self.scr_w, self.scr_h))
        self.text_font = self.pygame.font.SysFont("leelawadeeui", 30)
        self.clock = self.pygame.time.Clock()

        self.is_running = True
    def recursive(self, root, pos, parameter, create_root = False):
        OFFSET_X,OFFSET_Y,RAD = parameter
        x,y = pos
        self.printText(root.data, pos)
        self.printCircle(pos,RAD,root.isLeaf())
        # self.pygame.draw.line(self.screen,(0,0,0),(400,0),(400,600))
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

        
    def loop(self):
        while self.is_running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.is_running = False
            self.clock.tick(60)
            self.screen.fill((255,255,255))
            # self.pygame.draw.circle(self.screen, (255,0,0), (400,20), 20)
            self.draw()
            self.pygame.display.update()
            

Draw("(A+B+E+!E+!A&(!A+B&!D))").loop()



            


        




    


