# question --> https://practice.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1

def printAl(arr,n):
    # your code here
    for i in range(0, len(arr), 2):
        print(arr[i], end = ' ')
        
    # TC: O(N); SC: O(1)