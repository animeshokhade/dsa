class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def check(self, C, A, mid):
        count = 0
        summ = 0
        for ele in C:
            summ += ele

            # condition to ascertain allocation of tasks to workers
            if summ > mid:
                count += 1
                summ = ele

            # even for the last allocation the summ should be <= mid
            if count == A:
                return False
        return True

    def paint(self, A, B, C):
        mod = 10000003
        floor = 0

        # transforming the input array
        C = [B * ele for ele in C]
        low = max(C)
        high = sum(C)

        while low <= high:
            mid = (low + high) // 2
            if self.check(C, A, mid):
                floor = mid
                high = mid - 1
            else:
                low = mid + 1

        return floor % mod

    # R = (sum - min) * B + 1
    # TC: O(NlogR); SC: O(1)
