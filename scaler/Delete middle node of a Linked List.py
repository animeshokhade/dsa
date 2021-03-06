# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if not A:
            return None

        siz = 0
        cur = A

        while cur:
            siz += 1
            cur = cur.next

        if siz == 1:
            return None

        slow, fast = A, A

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = A

        while pre.next != slow:
            pre = pre.next

        pre.next = pre.next.next

        return A

        # TC: O(N); SC: O(1)