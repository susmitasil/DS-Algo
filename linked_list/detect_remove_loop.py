class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        slowptr = fastptr = head
        
        while fastptr and slowptr:
            fastptr = fastptr.next
            
            if fastptr ==None or fastptr.next ==None:
                return
            
            fastptr = fastptr.next
            slowptr = slowptr.next
            if fastptr==slowptr:
                break
            # print(fastptr.next.next, slowptr)
        if fastptr==None or fastptr.next.next==None:
            return
        else:
            slowptr = head
            while fastptr!=slowptr:
            # print(fastptr.next)
                fastptr = fastptr.next
                slowptr = slowptr.next
            
            while fastptr.next!=slowptr:
                fastptr=fastptr.next
            
            fastptr.next = None
        