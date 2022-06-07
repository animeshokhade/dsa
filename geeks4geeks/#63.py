# question --> https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1/?page=2&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Sorting&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=Binary%20Search&category[]=number-theory&category[]=two-pointer-algorithm&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=Traversal&category[]=%20modular%20arithmetic&category[]=Merge%20Sort&category[]=Data%20Type&category[]=Data%20Structures&category[]=Puzzles&category[]=Kadane&category[]=Functions&category[]=Pointers&category[]=anagram&category[]=Factorization&category[]=Practice-Problems&category[]=Reverse&sortBy=submissions#

class Solution:
    def maxLen(self, n, arr):
        # Code here
        prefix_sum = 0
        size = 0
        looker = {}
        for index, a in enumerate(arr):
            prefix_sum += a
            if prefix_sum == 0:
                size = max(size, index + 1)
            if prefix_sum in looker:
                size = max(size, index - looker[prefix_sum])
                continue
            looker[prefix_sum] = index
        return size

    # TC: O(N); SC: O(N)
