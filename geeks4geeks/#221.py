# question --> https://practice.geeksforgeeks.org/problems/special-series-sum0903/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=accuracy#

class Solution:
    def natural(self, n):
        return (n * (n + 1)) // 2

    def sumOfTheSeries(self, n):
        # code here
        summ = 0
        for _ in range(1, n + 1):
            summ += self.natural(_)
        return summ

        # TC: O(N); SC: O(1)

# clean and optimised

class Solution:
    def sumOfTheSeries(self, n):
        # code here
        ret = (n * (n + 1) * (n + 2)) // 6
        return ret

        # TC: O(1); SC: O(1)