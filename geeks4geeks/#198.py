# question --> https://practice.geeksforgeeks.org/problems/operating-an-array/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    # Code here
    return x in a

# fucntion must return true if 
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    # Code here
    if 0 <= yi < len(a):
        a.insert(yi, y)
        return True
    return False 

# fucntion must return true if 
# deletion is successful or else
# return false
def deleteEle(a, z):
    # Code here
    if z in a: 
        ind = a.index(z)
        a.pop(ind)
    return True
    
# TC: O(N); SC: O(1)