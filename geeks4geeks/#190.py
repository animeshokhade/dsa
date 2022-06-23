# question --> https://practice.geeksforgeeks.org/problems/game-with-nos3123/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

def game_with_number (arr,  n) : 
    #Complete the function
    for i in range(n - 1):
        arr[i] = arr[i] ^ arr[i + 1]
        
    return arr
    # TC: O(N); SC: O(1)