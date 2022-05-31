# question --> https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        merged = []
        left, right = 0, n
        while right < 2 * n:
            merged.append(nums[left])
            left += 1
            merged.append(nums[right])
            right += 1
        return merged

    '''
    TC: O(N)
    SC: O(N)
    '''


