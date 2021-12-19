#Intersection point of 2 singly linked list


def intersetPoint(head1,head2):
    #code here
    l1= l2 = 0
    curr1,curr2 = head1,head2
    while curr1!=None:
        l1+=1
        curr1 = curr1.next
        
    while curr2!=None:
        l2+=1
        curr2 = curr2.next
    curr1,curr2 = head1,head2    
    
    if l1>l2:
        for i in range(l1-l2):
            curr1= curr1.next
    else:
        for i in range(l2-l1):
            curr2= curr2.next

            
    while curr1 != curr2:
        curr1 = curr1.next
        curr2= curr2.next
        
    return curr1.data