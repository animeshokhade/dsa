# question --> https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1/?page=1&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Sorting&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=Binary%20Search&category[]=number-theory&category[]=two-pointer-algorithm&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=Traversal&category[]=%20modular%20arithmetic&category[]=Merge%20Sort&category[]=Data%20Type&category[]=Data%20Structures&category[]=Puzzles&category[]=Kadane&category[]=Functions&category[]=Pointers&category[]=anagram&category[]=Factorization&category[]=Practice-Problems&category[]=Reverse&sortBy=submissions#

class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):

        # code here
        temp = set()
        for _ in a:
            temp.add(_)

        for _ in b:
            temp.add(_)

        return len(temp)

    # TC: O(n + m); SC: O(max(n, m))
