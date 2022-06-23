# question --> https://practice.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
def insertInMid(head,node):
    #code here
    siz = 0
    cur = head 
    
    while cur: 
        siz += 1
        cur = cur.next
        
    ins = siz // 2 

    i = 0
    cur = head
    while cur: 
        if (siz & 1 and i == ins) or (siz % 2 == 0 and i == ins - 1):
            node.next = cur.next
            cur.next = node 
        cur = cur.next
        i += 1
        
    # TC: O(N); SC: O(1)