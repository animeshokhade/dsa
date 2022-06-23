# question --> https://practice.geeksforgeeks.org/problems/identical-linked-lists/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    l1, l2 = head1, head2
    
    while l1 and l2: 
        if l1.data != l2.data: 
            return 0
        l1 = l1.next
        l2 = l2.next
        
    return 1
    
    # TC: O(N); SC: O(1)