from Stack import *
class Operator():
    def __init__(self,express):
        self.express = express
        self.postfix = []
        self.__to_posfix()
    def __to_posfix(self):
        mystack = Stack()
        prec = {'(':0, '!':1, '&':2, '+':3}
        operator_list = ['(', '!', '&', '+', ')']
        token_list = self.express
        bracket_flag = False
        temp_char = ""
        for token in token_list:
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
                    top_token = mystack.pop()
                    while top_token != '(':
                        self.postfix.append(top_token)
                        top_token = mystack.pop() 
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


if __name__ == "__main__":
    Operator("(((I0&I1&!I2)+!I1)+I3)") 