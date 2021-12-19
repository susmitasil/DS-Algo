#Implement queue with linked list

class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        if self.front is None :
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
        self.size +=1
        print(data, 'inserted')

    def deQueue(self):
        if self.front is None or self.rear is None:
            print('Queue Underflow!')
            return -1
        temp = self.front.data
        self.front = self.front.next
        self.size -=1
        if self.size == 0:
            self.front = self.rear = None
        return temp

    def getFront(self):
        if self.front is None :
           print('Queue is Empty')
        else:
            return self.front.data
    
    def getRear(self):
        if self.rear is None :
           print('Queue is Empty')
        else:
            return self.rear.data

    def getSize(self):
        return self.size


if __name__ == '__main__':
    queue = Queue()
    queue.enQueue(3)
    queue.enQueue(8)
    queue.enQueue(5)
    queue.enQueue(7)
    queue.enQueue(2)
    print(queue.getSize())
    print(queue.getFront())
    print(queue.getRear())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())

