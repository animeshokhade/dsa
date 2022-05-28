class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] *= n

        for j in range(n):
            index = A[j] // n
            val = A[index] // n
            A[j] += val

        for k in range(n):
            A[k] %= n

        return A

