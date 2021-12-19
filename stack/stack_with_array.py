#Implement stack with simple array

class Stack:
    def __init__(self, Capcity=1):
        self.top = -1
        self.Capcity = Capcity
        self.A = [None]*Capcity

    def push(self, data):
        if self.top+1 >= self.Capcity:
            print('Stack Overflow, cannot push')
            return
        self.top = self.top+1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print('Stack Underflow, cannot pop')
            return
        temp = self.A[self.top]
        self.A[self.top] = None
        self.top -=1
        return temp

    def top(self):
        if self.top == -1:
            print('Stack Undeflow')
            return
        return self.A[self.top]

    def size(self):
        curr = self.top
        count = 0
        while curr>=0:
            count+=1
            curr-=1
        return count
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top+1 == self.Capcity


if __name__ == '__main__':
    stack = Stack(3)
    print(stack.isEmpty())
    print('=====')
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(4)
    stack.push(5)
    print(stack.size())
    print(stack.isFull())
    print(stack.pop())