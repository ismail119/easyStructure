class PriorityQueue:
    def __init__(self,firstNode):
        self.queue = [firstNode]

    def enqueueAll(self,nodeList):
        for i in nodeList: self.enqueue(i)

    def enqueue(self,node):
        self.queue.append(node)
        self.queue = sorted(self.queue,key=node.weight)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue)==0
