class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # spf reference sieve for prime factorisation
        ceil = max(A)
        spf = [0] * (ceil + 1)

        # marking the sieve
        for i in range(ceil + 1):
            spf[i] = i

            # prime filter
        stepper = 2
        while stepper * stepper <= ceil:
            if spf[stepper] == stepper:
                # prime number
                expunge = stepper * stepper
                while expunge <= ceil:
                    if spf[expunge] == expunge:
                        spf[expunge] = stepper
                    expunge += stepper
            stepper += 1

        # to track distinct prime factors
        distinct_prime_divisors = set()

        for a in A:
            while a > 1:
                div = spf[a]
                distinct_prime_divisors.add(div)
                while a % div == 0:
                    a //= div

        return len(distinct_prime_divisors)


'''
M -> max element in the array
N -> array size
TC: O(NlogM + loglogM) => O(NlogM)
SC: O(logM) 
'''