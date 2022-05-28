class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        window = dict()

    n = len(A)

    for index in range(B):
        if A[index] in window:
            window[A[index]] += 1
        else:
            window[A[index]] = 1

    iterations = n - B + 1
    ans = list()
    start, end = 0, B - 1

    for _ in range(iterations):
        ans.append(len(window))
        window[A[start]] -= 1
        if window[A[start]] == 0:
            del window[A[start]]
        start += 1
        end += 1
        if end < n:
            if A[end] in window:
                window[A[end]] += 1
            else:
                window[A[end]] = 1

    return ans












