# question --> https://practice.geeksforgeeks.org/problems/third-largest-element/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

class Solution:
    def thirdLargest(self,a, n):
        # code here
        l1, l2, l3 = 0, 0, 0
        for ele in a: 
            if ele > l1: 
                l3 = l2
                l2 = l1
                l1 = ele
            elif l1 > ele > l2: 
                l3 = l2
                l2 = ele
            elif ele > l3: 
                l3 = ele
        return l3
        
        # TC: O(N); SC: O(1)