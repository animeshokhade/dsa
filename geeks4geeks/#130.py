# question --> https://practice.geeksforgeeks.org/problems/decimal-to-any-base-conversion2440/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def getNumber(self, B, N):
        # code here
        ans = ''
        while N:
            dig = N % B
            if dig < 10:
                ans += str(dig)
            else:
                ans += chr(ord('A') - 10 + dig)
            N //= B
        return str(ans[::-1])

    # TC: O(logN); SC: O(1)