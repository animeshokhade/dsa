# question --> https://practice.geeksforgeeks.org/problems/circular-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

def isCircular(head):
    # Code here
    if not head:
        return True

    cur = head
    while True:
        cur = cur.next

        if not cur:
            return False

        if cur.next == head:
            return True

    # TC: O(N); SC: O(1)