# question --> https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cf = 0
        head = ListNode()
        cur = head
        
        while cf or l1 or l2: 
            if l1: 
                cf += l1.val
                l1 = l1.next
            
            if l2: 
                cf += l2.val
                l2 = l2.next
            
            dig = cf % 10
            
            cur.next = ListNode(dig)
            cur = cur.next
            
            cf //= 10
            
        return head.next
    
    # TC: O(N); SC: O(1)