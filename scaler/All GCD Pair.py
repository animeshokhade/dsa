import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort(reverse = True)
        n = len(A)
        ans = []
        count = {}
        for i in range(n):
            if (count.get(A[i]) != None and count[A[i]] > 0):
                count[A[i]] -= 1
            else:
                for j in range(len(ans)):
                    gcd = math.gcd(ans[j], A[i]);
                    if count.get(gcd) == None:
                        count[gcd] = 2
                    else:
                        count[gcd] += 2
                ans.append(A[i])
        return ans

'''
GCD of 2 numbers will always be less than or equal to the lesser of the 2 numbers.
So, the input array, can be reverse sorted so that the 1st element would be the largest
number. Now, the largest number would always be in the answer array as the GCD of any
combination can't be greater than it.

So, we take the largest element and add that to the answer array. Now we calculate
GCD of elements of answer array with the ith element of A (on which we are iterating).

For ith element GCD with jth element of answer array renders 2 pairs of same GCD. 
These values must now be ignored in the input array as they represent GCD of two elements
and thus won't be appended to the answer array. 

So, we keep a hashmap to track GCDs. For ith element, if it is a GCD which has a
non-negative count, we ignore it and reduce its count. When the GCD of ith A and jth ans
element is not present in the hashmap or has a count of 0 we append it to the answer
array. 
'''

# alternate approach

import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort(reverse=True)
        n = len(A)
        ans = []
        count = {}
        for i in range(n):
            if (count.get(A[i]) != None and count[A[i]] > 0):
                count[A[i]] -= 1
            else:
                for j in range(len(ans)):
                    gcd = math.gcd(ans[j], A[i]);
                    if count.get(gcd) == None:
                        count[gcd] = 2
                    else:
                        count[gcd] = count[gcd] + 2

                ans.append(A[i]);
        return ans

# alternate approach

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)


import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort(reverse=True)
        n = len(A)
        vec = []
        cnt = {}
        for i in range(n):
            if (cnt.get(A[i]) != None and cnt[A[i]] > 0):
                cnt[A[i]] = cnt[A[i]] - 1
            else:
                for j in range(len(vec)):
                    gcd = math.gcd(vec[j], A[i]);
                    if cnt.get(gcd) == None:
                        cnt[gcd] = 2
                    else:
                        cnt[gcd] = cnt[gcd] + 2

                vec.append(A[i]);
        return vec;

