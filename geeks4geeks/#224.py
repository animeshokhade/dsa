# question --> https://practice.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

# Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    # Code here
    node = Node(data)

    i = 0
    cur = head
    while True:
        if i == p:
            node.prev = cur
            if cur.next:
                node.next = cur.next
                cur.next.prev = node
            cur.next = node
            return head
        i += 1
        cur = cur.next

    # TC: O(N); SC: O(1)
