# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        cur = A

        bef = None
        aft = None
        cnt = 0

        while cur and cnt < B:
            aft = cur.next
            cur.next = bef
            bef = cur
            cur = aft
            cnt += 1

        if aft:
            A.next = self.reverseList(aft, B)

        return bef

    # TC: O(N); SC: O(N)

# optimised

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        n = len(A)
        rec = 0
        temp = 0
        area = 0

        ind = 0
        while ind < n:
            if not stack or A[ind] >= A[stack[-1]]:
                stack.append(ind)
                ind += 1
            else:
                temp = stack.pop()
                area = A[temp] * (ind if not stack else ind - stack[-1] - 1)
                rec = max(rec, area)

        while stack:
            temp = stack.pop()
            area = A[temp] * (ind if not stack else ind - stack[-1] - 1)
            rec = max(area, rec)

        return rec

        # TC: O(N); SC: O(N)

# clean and optimised

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def reverseList(self, A, B):
        if not A or not A.next:
            return A

        length = self.get_length(A)
        dummy = ListNode(0)
        prev = dummy
        dummy.next = A
        curr = A

        for _ in range(length // B):
            for _ in range(B - 1):
                aft = curr.next
                curr.next = aft.next
                aft.next = prev.next
                prev.next = aft
            prev = curr
            curr = curr.next

        return dummy.next

    # TC: O(N); SC: O(1)
