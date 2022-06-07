# question --> https://practice.geeksforgeeks.org/problems/square-root/1/?page=2&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Sorting&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=Binary%20Search&category[]=number-theory&category[]=two-pointer-algorithm&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=Traversal&category[]=%20modular%20arithmetic&category[]=Merge%20Sort&category[]=Data%20Type&category[]=Data%20Structures&category[]=Puzzles&category[]=Kadane&category[]=Functions&category[]=Pointers&category[]=anagram&category[]=Factorization&category[]=Practice-Problems&category[]=Reverse&sortBy=submissions

class Solution:
    def floorSqrt(self, x):
    #Your code here
        floor = 0
        temp = x
        is_lower = False
        while True:
            if not is_lower:
                temp //= 2
            if temp * temp == x:
                return temp
            if temp * temp < x:
                floor = temp
                temp += 1
                is_lower = True
            if is_lower:
                if temp * temp > x:
                    break
        return floor

    # TC: O(logN); SC: O(1)
    