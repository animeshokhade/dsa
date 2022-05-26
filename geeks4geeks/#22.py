# question --> https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1/?page=1&status[]=unsolved&sortBy=submissions#

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        temp = head
        size = 1
        while temp.next:
            temp = temp.next
            size += 1
        if size == 1: return head.data
        mid = size // 2
        temp = head
        for _ in range(mid):
            temp = temp.next
            ans = temp.data
        return ans

        # TC:O(N); SC:O(1)
# end 