# question --> https://practice.geeksforgeeks.org/problems/product-of-array-element/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

def product(arr,n,mod):
    # your code here
    mul = 1
    for ele in arr: 
        mul *= ele
        mul %= mod
    return mul % mod 
    
    # TC: O(N); SC: O(1)