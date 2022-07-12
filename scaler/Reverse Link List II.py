# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverse(self, node):
        aft = None
        bef = None
        while node:
            aft = node.next
            node.next = bef
            bef = node
            node = aft


    def reverseBetween(self, A, B, C):
        if not A or not A.next:
            return A

        cur = A
        cnt = 0
        start = None
        end = None
        first = None
        last = None

        while cur:
            cnt += 1

            if cnt < B:
                first = cur

            if cnt == B:
                start = cur

            if cnt == C:
                end = cur
                last = end.next
                break  # no need to traverse anymore

            cur = cur.next

        end.next = None
        self.reverse(start)

        if first:
            first.next = end
        else:
            A = end

        start.next = last
        return A

    # TC: O(N); SC: O(1)

# alternative approach

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if not A or not A.next:
            return A

        dummy = ListNode(0)
        dummy.next = A
        prev = dummy

        for _ in range(B - 1):
            prev = prev.next

        tail = prev.next

        for _ in range(C - B):
            cache = tail.next
            tail.next = cache.next
            cache.next = prev.next
            prev.next = cache

        return dummy.next

        # TC: O(N); SC: O(1)