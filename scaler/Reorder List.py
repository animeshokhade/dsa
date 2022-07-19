# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def mid(self, A):
        slow, fast = A, A

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def reverse(self, A):
        pre = None
        cur = A
        aft = None

        while cur:
            aft = cur.next
            cur.next = pre
            pre = cur
            cur = aft

        return pre


    def reorderList(self, A):
        mid = self.mid(A)

        R = mid.next
        mid.next = None

        R = self.reverse(R)

        cur = A
        state = 1

        while cur:
            if state:
                temp = cur
                cur = cur.next
                temp.next = R
                state ^= 1
            else:
                temp = R
                R = R.next
                temp.next = cur
                state ^= 1

        return A

    # TC: O(N); SC: O(1)