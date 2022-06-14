# question --> https://practice.geeksforgeeks.org/problems/compete-the-skills5807/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        n = len(a)
        ca, cb = 0, 0
        for index in range(n):
            if a[index] > b[index]:
                cc[0] += 1
            elif a[index] < b[index]:
                cc[1] += 1

        # TC: O(len(A) | len(B)); SC: O(1)
