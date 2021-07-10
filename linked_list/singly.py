class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llists = ''

        while itr:
            llists += str(itr.data) + ' ---> '  if itr.next else str(itr.data)
            itr = itr.next
        print(llists)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count +=1
            itr = itr.next
        print(count)
        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        print(node)
        self.head = node

    def insert_at_end(self,data):
        print(self.head)
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index <0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception('Invalid Index')

        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, arr):
        self.head = None
        for data in arr :
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning('abc')
    ll.insert_at_end('def')
    ll.insert_at_end('pqr')
    ll.print()
    ll.get_length()
    ll.insert_at(0,'mno')
    ll.insert_at(2,'xyz')
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.insert_values([45,7,12,567,99])
    ll.print()