#Implement stack with dynamic array

class Stack:
    def __init__(self, Capcity=1):
        self.top = -1
        self.Capcity = Capcity
        self.A = [None]*Capcity

    def push(self, data):
        if self.top+1 == self.Capcity:
            print('Trying to resize')
            self.resize()
        if self.isFull():    
            return 'Stack Overflow, cannot push'
        self.top = self.top+1
        self.A[self.top] = data
        print(self.A[self.top])

    def pop(self):
        if self.top == -1:
            # print('Stack Underflow, cannot pop')
            return 'Stack Underflow, cannot pop'
        temp = self.A[self.top]
        self.A[self.top] = None
        self.top -=1
        if self.top< self.Capcity//2:
            self.resize('half')
        return temp

    def top(self):
        if self.top == -1:
            # print('Stack Undeflow')
            return 'Stack Undeflow'
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

    def resize(self, r_type='double'):
        if r_type == 'half':
            self.Capcity= self.Capcity//2
            new_A = [None]*(self.Capcity)
            
            for i in range(self.top+1):
                new_A[i] = self.A[i]
            self.A = new_A
            print('resized to half')

        else:
            self.Capcity= self.Capcity*2
            new_A = [None]*(self.Capcity)
            if new_A is None:
                print('Use bigger machine')
                return
            for i in range(self.top+1):
                new_A[i] = self.A[i]
            self.A = new_A
            print('resized to double')

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
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())