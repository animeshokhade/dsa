class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):

        # sieve bool --> generating prime numbers
        spf = [True] * (A + 1)
        spf[0], spf[1] = False, False

        i = 2
        while i * i <= A:
            if spf[i]:
                # prime number
                j = i * i
                while j <= A:
                    spf[j] = False
                    j += i
            i += 1

        # two pointer
        prime = []
        for index in range(len(spf)):
            if spf[index]:
                prime.append(index)

        start, end = 0, len(prime) - 1
        while start <= end:
            if prime[start] + prime[end] < A:
                start += 1
            elif prime[start] + prime[end] > A:
                end -= 1
            else:
                return [prime[start], prime[end]]


'''
2 pointers is better because in set approach we traverse the sieve again while
here the new array (significantly smaller) is traversed.
Two, Three, Four sum are usually solved using two pointers (or multiple) pointers
if the array is sorted otherwise, use set (for lookup).
TC: O(nloglogn) SC: O(n)  
'''


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A == 4: return [2, 2]

        # sieve bool --> generating prime numbers
        spf = [True] * (A + 1)
        spf[0], spf[1] = False, False

        i = 2
        while i * i <= A:
            if spf[i]:
                # prime number
                j = i * i
                while j <= A:
                    spf[j] = False
                    j += i
            i += 1

        # hashSet
        lookup = set()
        for p in range(len(spf)):
            if spf[p]:
                lookup.add(p)

        for index in range(len(spf)):
            if spf[index]:
                if A - index in lookup:
                    return [index, A - index]

