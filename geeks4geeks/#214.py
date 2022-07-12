# question --> https://practice.geeksforgeeks.org/problems/play-with-or5515/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Bit%20Magic&sortBy=submissions#

def game_with_number(arr, n):
    # Complete the function
    for i in range(n - 1):
        arr[i] = arr[i] | arr[i + 1]
    return arr

    # TC: O(N); SC: O(1)