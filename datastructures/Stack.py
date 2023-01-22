class Stack:
    def __init__(self,firstNode):
        self.stack = [firstNode]

    def push(self,index):
        self.stack.append(index)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack)==0
