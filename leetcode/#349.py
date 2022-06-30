# question --> https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))

    # TC: O(min(nums1, nums2)); SC: O(|nums1| + |nums2|)

# intersection implementation

from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lkp = Counter(nums1)
        ret = []

        for num in nums2:
            if num in lkp:
                ret.append(num)
                lkp.pop(num)

        return ret

# TC: O(min(nums1, nums2)); SC: O(|nums1| + |nums2|)