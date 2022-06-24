# question --> https://www.codechef.com/submit/DETSCORE

T = int(input())
score = 0
for tc in range(T): 
    n, p = map(int, input().split())
    n //= 10
    score = n * p 
    print(score) 