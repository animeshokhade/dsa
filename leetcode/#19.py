# question --> https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []

        cur = head
        siz = 0

        while cur:
            siz += 1
            cur = cur.next

        if n == siz:
            head = head.next
            return head

        pre = siz - n
        cur = head

        i = 1
        while cur and i != pre:
            i += 1
            cur = cur.next

        if cur and cur.next:
            cur.next = cur.next.next
        return head

        # TC: O(N); SC: O(1)

# clean code

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head

        # TC: O(N); SC: O(1)