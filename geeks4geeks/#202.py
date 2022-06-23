# question --> https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum1555/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

def multiply (arr, n) : 
    #Complete the function
    m = n // 2
    l, r = 0, 0
    
    for ind, ele in enumerate(arr):
        if ind < m: 
            l += ele
        else: 
            r += ele
            
    return l * r
    
    # TC: O(N); SC: O(1)