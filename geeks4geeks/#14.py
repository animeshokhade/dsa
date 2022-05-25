# question --> https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1/?page=1&category[]=Arrays&category[]=Mathematical&category[]=Strings&category[]=Hash&category[]=Bit%20Magic&category[]=Matrix&category[]=Recursion&category[]=Prime%20Number&category[]=Numbers&category[]=number-theory&category[]=Modular%20Arithmetic&category[]=sieve&category[]=Combinatorial&category[]=sliding-window&category[]=palindrome&category[]=pattern-printing&category[]=Fibonacci&category[]=Geometric&category[]=permutation&category[]=logical-thinking&category[]=Binary%20Representation&category[]=prefix-sum&category[]=factorial&category[]=set&category[]=Operators&category[]=%20modular%20arithmetic&category[]=Division&category[]=subset&category[]=Data%20Type&category[]=Functions&category[]=Puzzles&category[]=Kadane&category[]=Reverse&curated[]=1&sortBy=submissions

class Solution:
#Function to check if two arrays are equal or not.
  #return: True or False
  
  #code here
  def check(self,A,B,N):
    lookup = {}
    for a in A: 
      if a in lookup: 
        lookup[a] += 1
      else: 
        lookup[a] = 1
    for b in B: 
        if b in lookup: 
          lookup[b] -= 1
        if lookup[b] == 0: 
          del lookup[b]
        else: 
          lookup[b] = 1
    if not len(lookup): return 1
    return 0
      
# TC: O(N); SC: O(N)
# end 