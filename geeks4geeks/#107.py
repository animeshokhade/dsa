# question --> https://practice.geeksforgeeks.org/problems/even-odd-sum5450/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def EvenOddSum(self, N, Arr):
        # code here (return list)
        odd, even = 0, 0
        for index in range(N):
            if index & 1:
                odd += Arr[index]
            else:
                even += Arr[index]
        return even, odd

        # TC: O(N); SC: O(1)

