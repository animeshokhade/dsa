# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        dummy = ListNode(0)
        temp = dummy

        while A and B:
            if A.val < B.val:
                temp.next = A
                temp = temp.next
                A = A.next
            else:
                temp.next = B
                temp = temp.next
                B = B.next

        while A:
            temp.next = A
            temp = temp.next
            A = A.next

        while B:
            temp.next = B
            temp = temp.next
            B = B.next

        return dummy.next

        # TC: O(A + B); SC: O(1) 