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