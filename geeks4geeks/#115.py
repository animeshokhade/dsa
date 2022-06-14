# question --> https://practice.geeksforgeeks.org/problems/compete-the-skills5807/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        for a, b in zip(a, b):
            if a > b:
                cc[0] += 1
            elif b > a:
                cc[1] += 1

    # TC: O(N); SC: O(1)
