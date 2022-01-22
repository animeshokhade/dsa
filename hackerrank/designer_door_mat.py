# question --> https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=profile
# my_code
N, M = map(int, input().split())
row = 0
row_upper = 1
multiplier = 1
string = '.|.'
temp = multiplier*string
message = 'WELCOME'

while(row < N):
    if(row < N//2):
        print(temp.center(M, '-'))
        if(row != N//2 - 1):
            multiplier += 2
            temp = multiplier*string
    if(row == N//2):
        print(message.center(M, '-'))
    if(row > N//2):
        print(temp.center(M, '-'))
        multiplier -= 2
        temp = multiplier*string
    row += 1

# end