# question --> https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1/?page=2&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Sorting&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=Binary%20Search&category[]=number-theory&category[]=two-pointer-algorithm&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=Traversal&category[]=%20modular%20arithmetic&category[]=Merge%20Sort&category[]=Data%20Type&category[]=Data%20Structures&category[]=Puzzles&category[]=Kadane&category[]=Functions&category[]=Pointers&category[]=anagram&category[]=Factorization&category[]=Practice-Problems&category[]=Reverse&sortBy=submissions#

def rotate( arr, n):
    swap = 0
    while swap < n - 1:
        arr[swap], arr[n - 1] = arr[n - 1], arr[swap]
        swap += 1
    return arr

    # TC: O(N); SC: O(1) 