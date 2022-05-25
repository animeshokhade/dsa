# question --> https://practice.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1/?page=1&status[]=unsolved&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=number-theory&category[]=Modular%20Arithmetic&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=set&category[]=Operators&category[]=Division&category[]=subset&category[]=Data%20Type&category[]=Functions&category[]=Puzzles&category[]=Kadane&category[]=Reverse&category[]=%20modular%20arithmetic&curated[]=1&sortBy=submissions#

class Solution:
  def firstElementKTime(self,  a, n, k):
    # code here
    lookup = {}
    for ele in a: 
      if ele in lookup: 
        lookup[ele] += 1
        if lookup[ele] == k: return ele
      else: 
        lookup[ele] = 1
        if k == 1: return ele 
    return -1
  
# TC: O(N); SC: O(N)
# end 