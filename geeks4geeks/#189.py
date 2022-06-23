# question --> https://practice.geeksforgeeks.org/problems/anagram-of-string/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

def remAnagram(str1,str2):
    
    #add code here
    s1 = [0] * 26
    s2 = [0] * 26
    
    for i, s in enumerate(str1): 
        ind = ord(s) - ord('a')
        s1[ind] += 1
        
    for i, s in enumerate(str2):
        ind = ord(s) - ord('a')
        s2[ind] += 1
        
    ans = 0
    
    for i in range(26): 
        ans += abs(s1[i] - s2[i])
        
    return ans 
    
    # TC: O(|str1| + |str2|); SC: O(1)