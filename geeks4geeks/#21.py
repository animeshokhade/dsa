# question --> https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1/?page=1&status[]=unsolved&sortBy=submissions#

'''
	Your task is to return the data stored in
	the nth node from end of linked list.

	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


# Function to find the data of nth node from the end of a linked list
def getNthFromLast(head, n):
    # code here
    size = 1
    temp = head
    while temp.next:
        temp = temp.next
        size += 1
    ans = -1
    if n > size:
        return ans
    elif n == size:
        return head.data
    loc = size - n
    temp = head
    for _ in range(loc):
        temp = temp.next
        ans = temp.data
    return ans

    # TC:O(N); SC:O(1)
# end 