# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def detectCycle(self, A):
        fast, slow = A, A

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: break

        if fast != slow: return None

        p1 = slow
        p2 = A

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

        # TC: O(N); SC: O(1)