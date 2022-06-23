# question --> https://practice.geeksforgeeks.org/problems/maximum-money2855/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def maximizeMoney(self, N , K):
        # code here 
        to = N * K
        ev = K * (N // 2)
        od = to - ev

        return max(od, ev)
        
    # TC: O(1); SC: O(1)