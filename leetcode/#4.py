# question --> https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        l = 0
        r = n1

        while l <= r:
            partition1 = (l + r) // 2
            partition2 = (n1 + n2 + 1) // 2 - partition1

            max_left_1 = float('-inf') if partition1 == 0 \
                else nums1[partition1 - 1]
            max_left_2 = float('-inf') if partition2 == 0 \
                else nums2[partition2 - 1]
            min_right_1 = float('inf') if partition1 == n1 else nums1[partition1]
            min_right_2 = float('inf') if partition2 == n2 else nums2[partition2]

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                return (max(max_left_1, max_left_2) + \
                        min(min_right_1, min_right_2)) / 2 if (n1 + n2) % 2 == 0 \
                    else max(max_left_1, max_left_2)

            elif max_left_1 > min_right_2:
                r = partition1 - 1

            else:
                l = partition1 + 1

        # TC: O(log(min(m, n))); SC: O(1)
