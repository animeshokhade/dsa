# question --> https://practice.geeksforgeeks.org/problems/sum-of-digits1742/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def sumOfDigits(self, N):
        # code here
        Sum = 0
        while N:
            Sum += N % 10
            N //= 10
        return Sum

    # TC: O(1); SC: O(1)
# end
