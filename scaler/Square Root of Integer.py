class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        floor = 0
        temp = A
        is_lower = False
        while True:
            # we only divide till temp * temp is greater than
            # or equal to A
            if not is_lower:
                temp //= 2
            if temp * temp == A:
                return temp
            elif temp * temp < A:
                floor = temp
                temp += 1
                is_lower = True
            # if temp * temp breaches A after having reduced
            # by division implies that we've found the floor
            elif is_lower:
                if temp * temp > A:
                    break
        return floor

        # TC: O(logN); SC: O(1)

# standard binary search
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low = 0
        high = A
        floor = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == A:
                return mid
            elif mid * mid < A:
                floor = mid
                low = mid + 1
            else:
                high = mid - 1
        return floor

        # TC: O(logN); SC: O(1)
