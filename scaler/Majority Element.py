class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majority = A[0]
        count = 1
        for i in range(1, len(A)):
            if majority == A[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = A[i]
                    count = 1

        return majority
