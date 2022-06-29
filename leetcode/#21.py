# question --> https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        temp = merged

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            temp.next = list1

        elif list2:
            temp.next = list2

        return merged.next

        # TC: O(|list1| + |list2|); SC: O(1)

# recursion

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        merged = ListNode()

        if list1.val < list2.val:
            merged = list1
            list1.next = self.mergeTwoLists(list1.next, list2)

        else:
            merged = list2
            list2.next = self.mergeTwoLists(list1, list2.next)

        return merged

        # TC: O(|list1| + |list2|); SC: O(|list1| + |list2|)

'''
l1 = 2 -> 5 -> 9 -> 12 -> 15 -> 20 -> None
l2 = 3 -> 7 -> 10 -> 17 -> 22 -> None

Recursion Simulation: 

Call 01: MTL(2, 3)
    merged = LN()
    if ...
    
    merged = ref(2)
    l1.next = MTL(5, 3)
    
    2 -> l1.next
    
Call 02: MTL(5, 3)     
    merged = LN()
    else ...
    
    merged = ref(3)
    l2.next = MTL(5, 7)
    
    3 -> l2.next

Call 03: MTL(5, 7)
    merged = LN()
    if ...
    
    merged = ref(5)
    l1.next = MTL(9, 7)
    
    5 -> l1.next
    
Call 04: MTL(9, 7)
    merged = LN()
    else ...
    
    merged = ref(7)
    l2.next = MTL(9, 10)
    
    7 -> l2.next
    
Call 05: MTL(9, 10)
    merged = LN()
    if ...
    
    merged = ref(9)
    l1.next = MTL(12, 10)
    
    9 -> l1.next
    
Call 06: MTL(12, 10)
    merged = LN()
    else ...
    
    merged = ref(10)
    l2.next = MTL(12, 17)
    
    10 -> l2.next
    
Call 07: MTL(12, 17)
    merged = LN()
    if ...
    
    merged = ref(12)
    l1.next = MTL(15, 17)
    
    12 -> l1.next 
    
Call 08: MTL(15, 17)
    merged = LN()
    if ...
    
    merged = ref(15)
    l1.next = MTL(20, 17)
    
    15 -> l1.next
    
Call 09: MTL(20, 17)
    merged = LN()
    else ...
    
    merged = ref(17)
    l2.next = MTL(20, 22)
    
    17 -> l2.next 
    
Call 10: MTL(20, 22)
    merged = LN()
    if ...
    
    merged = ref(20)
    l1.next = MTL(None, 22)
    
    20 -> l1.next
    
Base Hit: l1 None
    return l2
    
Call 10: contd.
    l1.next = ref(22)
    
    merged = 20 -> 22
    
Call 09: contd.
    l2.next = ref(20)
    
    merged = 17 -> 20 -> 22

Call 08: contd.
    l1.next = ref(17)
    
    merged = 15 -> 17 -> 20 -> 22
    
Call 07: contd. 
    l1.next = ref(15)
    
    merged = 12 -> 15 -> 17 -> 20 -> 22
    
Call 06: contd.
    l2.next = ref(12)
    
    merged = 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 05: contd.
    l1.next = ref(10)
    
    merged = 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 04: contd. 
    l2.next = ref(9)
    
    merged = 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 03: contd. 
    l1.next = ref(7)
    
    merged = 5 -> 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 02: contd. 
    l2.next = ref(5)
    
    merged = 3 -> 5 -> 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 01: contd.
    l1.next = ref(3)
    
    merged = 2 -> 3 -> 5 -> 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
return merged  
'''


# recursive - clean

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

        # TC: O(|list1| + |list2|); SC: O(|list1| + |list2|)

'''

l1 = 2 -> 5 -> 9 -> 12 -> 15 -> 20 -> None
l2 = 3 -> 7 -> 10 -> 17 -> 22 -> None

Recursion Simulation: 

Call 01: MTL(2, 3)
    l1.next = MTL(5, 3)
    
    2 -> l1.next
    
Call 02: MTL(5, 3)
    l1 = 3
    l2 = 5
    
    l1.next = MTL(7, 5)
    
    3 -> l1.next
    
Call 03: MTL(7, 5)
    l1 = 5
    l2 = 7
    
    l1.next = MTL(9, 7)
    
    5 -> l1.next
    
Call 04: MTL(9, 7)
    l1 = 7
    l2 = 9
    
    l1.next = MTL(10, 9)
    
    7 -> l1.next
    
Call 05: MTL(10, 9)
    l1 = 9
    l2 = 10
    
    l1.next = MTL(12, 10)
    
    9 -> l1.next
    
Call 06: MTL(12, 10)
    l1 = 10
    l2 = 12
    
    l1.next = MTL(17, 12)
    
    10 -> l1.next 
    
Call 07: MTL(17, 12)
    l1 = 12
    l2 = 17
    
    l1.next = MTL(15, 17)
    
    12 -> l1.next
    
Call 08: MTL(15, 17)
    l1.next = MTL(20, 17)
    
    15 -> l1.next
    
Call 09: MTL(20, 17)
    l1 = 17
    l2 = 20
    
    l1.next = MTL(22, 20)
    
    17 -> l1.next
    
Call 10: MTL(22, 20)
    l1 = 20
    l2 = 22
    
    l1.next = MTL(None, 22)
    
    20 -> l1.next
    
Base Hit: return 22

Call 10: contd.
    l1.next = 22
    
    20 -> 22
    
Call 09: contd.
    l1.next = 20
    
    17 -> 20 -> 22 
    
Call 08: contd.
    l1.next = 17
    
    15 -> 17 -> 20 -> 22
    
Call 07: contd.
    l1.next = 15
    
    12 -> 15 -> 17 -> 20 -> 22
    
Call 06: contd.
    l1.next = 12
    
    10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 05: contd.
    l1.next = 10
    
    9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 04: contd. 
    l1.next = 9
    
    7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 03: contd.
    l1.next = 7
    
    5 -> 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
Call 02: contd.
    l1.next = 5
    
    3 -> 5 -> 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22  
    
Call 01: contd.
    l1.next = 3
    
    l1 = 2 -> 3 -> 5 -> 7 -> 9 -> 10 -> 12 -> 15 -> 17 -> 20 -> 22
    
return l1
'''