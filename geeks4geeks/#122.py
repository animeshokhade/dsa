# question --> https://practice.geeksforgeeks.org/problems/distance-between-2-points3200/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

import math


class Solution:
    def distance(self, x1, y1, x2, y2):
        # Code here
        ans = round(math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)))
        return ans

        # TC: O(logN); SC: O(1)
