# question --> https://leetcode.com/problems/find-pivot-index/

class Solution():
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for index, num in enumerate(nums):
            if(leftsum == (S - leftsum - num)):
                return index
                break
            leftsum += num
        return -1
        
        # TC: O(N); SC: O(1)
        
# end