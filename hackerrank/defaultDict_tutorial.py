# question --> https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().strip().split())

from collections import defaultdict

A = defaultdict(list)

for i in range(n):
    A[input()].append(str(i + 1))

for key in range(m):
    b = input().strip()
    if b in A:
        print(' '.join(A[b]))
    else:
        print(-1)