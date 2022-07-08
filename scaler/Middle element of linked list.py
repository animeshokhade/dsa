# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        if not A or not A.next:
            return None

        slow, fast = A, A

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val

        # TC: O(N); SC: O(1)
