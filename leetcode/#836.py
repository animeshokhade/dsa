# question --> https://leetcode.com/problems/rectangle-overlap/

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[3] <= rec2[1] or rec1[1] >= rec2[3] or rec1[2] <= rec2[0] or rec1[0] >= rec2[2]:
            return 0
        return 1
        
        # TC: O(1); SC: O(1)
        
# end 