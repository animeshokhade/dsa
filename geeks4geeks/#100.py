# question --> https://practice.geeksforgeeks.org/problems/determine-focal-length-of-a-spherical-mirror5415/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def findFocalLength(self, R, type):
        # Code here
        if type == 'convex':
            return int(-R // 2)
        return int(R // 2)

    # TC: O(1); SC: O(1)