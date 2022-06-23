# question --> https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

def isLengthEvenOrOdd(head):
    # Code here
    siz = 0
    
    while head: 
        siz += 1
        head = head.next
    
    if siz % 2: 
        return 1
    return 0
    
    # TC: O(N); SC: O(1)