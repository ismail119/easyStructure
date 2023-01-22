class Queue:
    def __init__(self,firstNode):
        self.queue = [firstNode]

    def enqueue(self,index):
        self.queue.append(index)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue)==0
