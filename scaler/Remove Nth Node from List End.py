# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        siz = 0

        if B == 0: return A

        cur = A
        while cur:
            siz += 1
            cur = cur.next

        if siz <= B:
            return A.next

        pre = siz - B

        i = 1
        cur = A
        while cur:
            if i == pre:
                cur.next = cur.next.next
                return A
            i += 1
            cur = cur.next

        # TC: O(N); SC: O(1)

# clean code

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if not A:
            return

        tail = A
        for _ in range(B):
            tail = tail if tail is None else tail.next

        if not tail:
            return A.next

        prev = A
        curr = A

        while tail:
            prev = curr
            curr = curr.next
            tail = tail.next

        prev.next = curr.next
        return A

    # TC: O(N); SC: O(1)