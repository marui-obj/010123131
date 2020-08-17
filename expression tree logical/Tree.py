from Operator import *
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