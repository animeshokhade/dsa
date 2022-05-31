# question --> https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lookup = {}
        good_pairs = 0
        for num in nums:
            if num in lookup:
                good_pairs += lookup[num]
                lookup[num] += 1
                continue
            lookup[num] = 1
        return good_pairs

    '''
    TC: O(N)
    SC: O(N)
    '''

