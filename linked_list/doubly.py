class Node:
    def __init__(self,data, prev=None, next=None) :
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_from_beginning(self):
        itr = self.head
        dl_string = ''
        while itr:
            dl_string += str(itr.data)+ "--->" if itr.next else str(itr.data)
            # print(itr.prev, itr.next) 
            itr = itr.next
        print(dl_string)

    def print_from_end(self):
        itr = self.tail
        dl_string = ''
        while itr:
            dl_string += str(itr.data)+ "--->" if itr.prev else str(itr.data)
            itr = itr.prev
        print(dl_string)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        print(count)
        return count

    def insert_at_beginning(self,data):
        node = Node(data,None,self.head)
        self.head = node
        self.tail = node
        
    def insert_at_end(self,data):
        if self.head==None:
            self.head = Node(data, None, self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data,itr,None)
        itr.next = node
        self.tail = node

    def remove_at(self,index):
        length =self.get_length()
        if index<0 or index>length :
            raise Exception('Invalid index')
            
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        if index == length-1 :
            self.tail = self.tail.prev
            self.tail.next =None

        mid = length//2
        if index <mid :
            print('at start')
            itr = self.head 
            count = 0
            while itr:
                print(count, index)
                if(count== index-1):
                
                    itr.next = itr.next.next
                    print('check ', itr.next)
                    itr.next.prev = itr
                    break
                
                itr= itr.next
                count+=1
        else :
            print('at end')
            itr = self.tail
            count = self.get_length() - 1
            while itr:
                if(count== index+1):
                    itr.prev = itr.prev.prev
                    itr.prev.next = itr
                    break
                count-=1
                itr= itr.prev

    def insert_elements(self, arr):
        self.head = None
        for data in arr :
            self.insert_at_end(data)

        
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning('banana')
    ll.insert_at_end('mango')
    ll.insert_at_end('litchi')
    ll.insert_at_end('papaya')
    ll.insert_at_end('guava')
    ll.print_from_beginning()
    # ll.print_from_end()
    # ll.get_length()
    ll.remove_at(0)
    ll.print_from_beginning()
    ll.remove_at(2)
    ll.print_from_beginning()
    ll.insert_elements([12,22,28,6,4,34,18])
    ll.print_from_beginning()
    ll.print_from_end()
    ll.remove_at(6)
    ll.print_from_end()