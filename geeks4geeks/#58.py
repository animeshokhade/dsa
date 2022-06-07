# question --> https://practice.geeksforgeeks.org/problems/peak-element/1/?page=1&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Sorting&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=Binary%20Search&category[]=number-theory&category[]=two-pointer-algorithm&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=Traversal&category[]=%20modular%20arithmetic&category[]=Merge%20Sort&category[]=Data%20Type&category[]=Data%20Structures&category[]=Puzzles&category[]=Kadane&category[]=Functions&category[]=Pointers&category[]=anagram&category[]=Factorization&category[]=Practice-Problems&category[]=Reverse&sortBy=submissions#

class Solution:
    def peakElement(self, arr, n):
        # Code here
        low = 0
        high = n - 1
        if n == 1: return 0
        if arr[-1] > arr[-2]:
            return n - 1
        if arr[0] > arr[1]:
            return 0

        while low <= high:
            mid = (low + high) // 2
            if mid > 0 and mid < n - 1 and arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid
            elif arr[mid] >= arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1

        return 0

    # TC: O(logN); SC: O(1)
