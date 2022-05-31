# question --> https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        big = []
        n = len(nums)
        for pointer1 in range(n):
            counter = 0
            for pointer2 in range(n):
                if nums[pointer1] > nums[pointer2]:
                    counter += 1
            big.append(counter)
        return big

    '''
    TC: O(N^2)
    SC: O(N)
    '''

    