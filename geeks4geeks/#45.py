# question --> https://practice.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def isDigitSumPalindrome(self, N):
        # code here
        temp = N
        Sum = 0
        while temp:
            Sum += temp % 10
            temp //= 10
        Sum = str(Sum)
        start, end = 0, len(Sum) - 1
        while start <= end:
            if Sum[start] != Sum[end]: return 0
            start += 1
            end -= 1
        return 1

    # TC: O(N); SC:O(1)
# end
