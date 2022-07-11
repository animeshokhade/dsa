# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if not A:
            return

        pre = None
        cur = A
        fut = A.next

        while cur:
            cur.next = pre
            pre = cur
            cur = fut
            if fut:
                fut = fut.next

        head = pre
        return head

    # TC: O(N); SC: O(1)

