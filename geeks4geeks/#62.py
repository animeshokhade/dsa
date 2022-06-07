# question --> https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1/?page=2&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Sorting&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=Binary%20Search&category[]=number-theory&category[]=two-pointer-algorithm&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=Traversal&category[]=%20modular%20arithmetic&category[]=Merge%20Sort&category[]=Data%20Type&category[]=Data%20Structures&category[]=Puzzles&category[]=Kadane&category[]=Functions&category[]=Pointers&category[]=anagram&category[]=Factorization&category[]=Practice-Problems&category[]=Reverse&sortBy=submissions

class Solution:

    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        ##Your code here
        # Return true or false
        prefix_sum = 0
        looker = set()

        for a in arr:
            prefix_sum += a
            if prefix_sum in looker:
                return True
            if prefix_sum == 0:
                return True
            looker.add(prefix_sum)
        return False

    # TC: O(N); SC: O(N)