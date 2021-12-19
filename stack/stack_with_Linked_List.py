#Implement stack with Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, Capcity=5):
        self.head = None
        self.Capcity = Capcity

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            print(data, 'is pushed into the stack')
            return
        temp = Node(data, self.head)
        self.head = temp
        print(data, 'is pushed into the stack')
        
    def pop(self):
        if self.head == None:
            print('Stack Underflow, stack is empty')
        temp = self.head.data
        self.head = self.head.next
        return temp

    def top(self):
        if self.head == None:
            print('Stack Underflow, stack is empty')
            raise IndexError
        return self.head.data

    def size(self):
        if self.head == None:
            return 0
        count = 0
        curr = self.head
        while curr :
            count +=1
            curr = curr.next
        return count
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.push(4)
    stack.push(6)
    print(stack.top())
    print(stack.size())
    print(stack.pop())


