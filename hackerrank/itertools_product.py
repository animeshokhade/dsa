# question --> https://www.hackerrank.com/challenges/itertools-product/problem

# my code

A = list(map(int, input().split()))
B = list(map(int, input().split())) 

ans = list()

# Generating the Cartesian Product
for a in A:
    for b in B:
        ans.append((a, b))

# Printing the Cartesian Product
for tup in range(len(ans)):
    print(ans[tup], end = ' ') 

# Complexity --> TC => O(N^2) SC => O(N)

# Editorial Solution
from itertools import product

A = map(int, input().split())
B = map(int, input().split()) 

for item in product(A, B):
    print(item, end = ' ') 

# Complexity --> TC => O(N^2) SC => O(N)

# end 
