class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        summ = 0
        ans = []
        for start, number in enumerate(C):
            summ = 0
            for end in range(start, A):
                summ += C[end]
                ans.append(summ)
        final_ans = 0
        for number in ans:
            if number <= B:
                final_ans = max(final_ans, number)
        return final_ans



