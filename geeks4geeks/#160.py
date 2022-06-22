# question --> https://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1/?page=5&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

def convertFive(n):
    # Code here
    tmp = n
    ret = 0
    fiv = 5
    base = 1

    while tmp:
        mod = tmp % 10

        if mod != 0:
            ret += mod * base
        else:
            ret += fiv

        base *= 10
        fiv *= 10
        tmp //= 10

    return ret

    # TC: O(logN base 10); SC: O(1)