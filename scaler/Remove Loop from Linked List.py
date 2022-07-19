# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        fast, slow = A, A

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: break

        p1 = A
        p2 = slow

        while p1.next != p2.next:
            p1 = p1.next
            p2 = p2.next

        p2.next = None

        return A

        # TC: O(N); SC: O(1) 