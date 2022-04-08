# question --> https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

# my code
shoes_num = int(input())
inventory = list(map(int, input().split()))
counter = dict()

# Storing the size and number of shoes of that size
for size in inventory:
    if size in counter:
        counter[size] += 1
    else:
        counter[size] = 1

# Iterating over the customer orders 
iterations_input = int(input()) 

receipt = 0

for bill in range(iterations_input):
    order = list(map(int, input().split())) 
    if order[0] in counter:
        receipt += order[1]
        counter[order[0]] -= 1
        if counter[order[0]] == 0:
            del counter[order[0]] 

print(receipt) 

# Complexity --> TC => O(N) SC => O(N) 

# end 