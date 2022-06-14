# question --> https://practice.geeksforgeeks.org/problems/surface-area-and-volume-of-cuboid0522/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def find(self, l, b, h):
        # Code here
        vol = l * b * h
        sur = 2 * (b * h + h * l + l * b)
        return [sur, vol]

    # TC: O(1); SC: O(1)
