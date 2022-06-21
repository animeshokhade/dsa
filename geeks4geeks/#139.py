# question --> https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

def find(arr, n, x):
    # code here
    lo, hi = 0, n - 1
    floor = -1
    ceil = -1

    # floor
    while lo <= hi:
        mi = (lo + hi) // 2
        if arr[mi] < x:
            lo = mi + 1
        elif arr[mi] >= x:
            floor = mi
            hi = mi - 1

    lo, hi = 0, n - 1
    # ceil
    while lo <= hi:
        mi = (lo + hi) // 2
        if arr[mi] <= x:
            ceil = mi
            lo = mi + 1
        elif arr[mi] > x:
            hi = mi - 1

    if arr[floor] != x:
        floor = -1

    if arr[ceil] != x:
        ceil = -1

    return floor, ceil

    # TC: O(logN); SC: O(1)
