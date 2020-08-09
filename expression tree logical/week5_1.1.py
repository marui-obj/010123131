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
        self.scr_w,self.scr_h = 800,600
        self.screen  = self.pygame.display.set_mode((self.scr_w, self.scr_h))
        self.text_font = self.pygame.font.SysFont("leelawadeeui", 48)
        self.clock = self.pygame.time.Clock()

        self.is_running = True
    def recursive(self,root,low,high,pos):
        NODE_OFFSET_X = 30
        NODE_OFFSET_Y = 60
        NODE_RAD = 20
        low += 1
        if low == high and root != None:
            label = self.text_font.render(root.data, 1, (0,0,0))
            self.screen.blit(label, pos)
            pass
        elif root == None:
            pass
        elif low == 1:
            label = self.text_font.render(root.data, 1, (0,0,0))
            self.screen.blit(label, (self.scr_w/2,20))
            if root.data == '!':
                return self.recursive(root.left,low,high,(self.scr_w/2, 20+NODE_OFFSET_Y+NODE_RAD))
            else:
                return self.recursive(root.left,low,high,((self.scr_w/2)-NODE_OFFSET_X-((high-1)*NODE_RAD),20+NODE_OFFSET_Y+NODE_RAD)),\
                    self.recursive(root.right,low,high,((self.scr_w/2)+NODE_OFFSET_X+((high-1)*NODE_RAD),20+NODE_OFFSET_Y+NODE_RAD))
        else:
            x,y = pos
            label = self.text_font.render(root.data, 1, (0,0,0))
            self.screen.blit(label, pos)
            if root.data == '!':
                return self.recursive(root.left,low,high,(x, y+NODE_OFFSET_Y+NODE_RAD))
            else:
                if root.left and root.right:
                    return self.recursive(root.left,low,high,(x-NODE_OFFSET_X-NODE_RAD, y+NODE_OFFSET_Y+NODE_RAD)),\
                    self.recursive(root.right,low,high,(x+NODE_OFFSET_X+NODE_RAD, y+NODE_OFFSET_Y+NODE_RAD))
                elif root.left:
                    return self.recursive(root.left,low,high,(x-NODE_OFFSET_X-NODE_RAD, y+NODE_OFFSET_Y+NODE_RAD))
                elif root.right:
                    return self.recursive(root.right,low,high,(x+NODE_OFFSET_X+NODE_RAD, y+NODE_OFFSET_Y+NODE_RAD))
      
    def draw(self):
        root = self.root[0]
        self.recursive(root,0,self.high,1)
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
            

Draw("A+!B").loop()



            


        




    


