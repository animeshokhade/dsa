# question --> https://practice.geeksforgeeks.org/problems/number-pattern0517/1/?page=3&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def string_generator(self, N):
        ret = str(N)
        while True:
            N -= 1
            if N == 0: break
            ret = str(N) + ret + str(N)
        return ret

    def numberPattern(self, N):
        # code here
        for num in range(1, N + 1):
            print(self.string_generator(num), end=' ')
        return ''

        # TC: O(N^2); SC: O(1)
