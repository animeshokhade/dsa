# question --> https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur: 
            while cur.next and cur.val == cur.next.val: 
                cur.next = cur.next.next
            cur = cur.next
            
        return head
    
    # TC: O(N); SC: O(1)