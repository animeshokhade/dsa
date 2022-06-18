# question --> https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=false

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

lst = input().split()
S, r = lst[0], int(lst[1])

p = list(permutations(S, r))
p.sort()

for s in p:
    print(''.join(list(s)))
