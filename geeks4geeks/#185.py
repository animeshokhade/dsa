# question --> https://practice.geeksforgeeks.org/problems/queue-reversal/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

def rev(q):
    #add code here
    stk = []
    while not q.empty(): 
        stk.append(q.queue[0])
        q.get()
        
    while stk: 
        q.put(stk[-1])
        stk.pop()
        
    return q
    
    # TC: O(N); SC: O(N)