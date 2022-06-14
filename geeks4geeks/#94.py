# question --> https://practice.geeksforgeeks.org/problems/area-of-rectange-right-angled-triangle-and-circle2600/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def getAreas(self, L , W , B , H , R):
        # code here
        rec = L * W
        tri = 0.5 * B * H
        cir = 3.14 * R * R
        return [int(rec), int(tri), int(cir)]

    # TC: O(1); SC: O(1)