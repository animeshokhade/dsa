class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):
        summ = ans = 0
        for index, number in enumerate(A):
            index_start, index_end = index + 1, len(A) - index
            frequency = index_start * index_end
            summ = number * frequency
            ans += summ
        return ans


