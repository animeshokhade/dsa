class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sorted_array = [i for i in range(1, n + 1)]
        sorted_array_square = [i * i for i in range(1, n + 1)]

        a_square = [i * i for i in A]

        # equation 01
        missing_number_minus_duplicate = sum(sorted_array) - sum(A)

        # equation 02
        missing_number_plus_duplicate = (sum(sorted_array_square) - sum(a_square)) // missing_number_minus_duplicate

        ans = [0] * 2
        ans = [(missing_number_plus_duplicate - missing_number_minus_duplicate) // 2,
               (missing_number_minus_duplicate + missing_number_plus_duplicate) // 2]

        return ans
