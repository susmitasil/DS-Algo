# Implement queue with simple Circular Array

class Queue:
    def __init__(self, limit = 3):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0
    
    def enQueue(self, data):
        if self.size >= self.limit:
            print('Queue Overflow!')
            return
        
        self.que.append(data)
        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size+=1
        print('Queue after enqueue', self.que)

    def deQueue(self):
        if self.size <= 0:
            print('Queue Underflow!')
            return -1
        #self.que.pop(0)    Not writing this here so that I can save auxiliary space by not using a temp
        self.size-=1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear= self.size-1
        return self.que.pop(0)

    def getFront(self):
        if self.front ==None:
            print('Sorry the queue is empty')
            return
        
        return self.que[self.front]

    def getRear(self):
        if self.rear ==None:
            print('Sorry the queue is empty')
            return
        return self.que[self.rear]

    def getSize(self):
        return self.size


if __name__ == '__main__':
    queue = Queue()
    queue.enQueue(3)
    queue.enQueue(8)
    queue.enQueue(5)
    queue.enQueue(7)
    print(queue.getSize())
    print(queue.getFront())
    print(queue.getRear())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())

