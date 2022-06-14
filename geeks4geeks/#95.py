# question --> https://practice.geeksforgeeks.org/problems/count-digits5716/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def evenlyDivides(self, N):
        # code here
        temp = N
        digits = 0
        while temp:
            if temp % 10 != 0 and N % (temp % 10) == 0:
                digits += 1
            temp //= 10
        return digits

    # TC: O(logN); SC: O(1)
