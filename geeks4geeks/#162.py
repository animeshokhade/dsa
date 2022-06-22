# question --> https://practice.geeksforgeeks.org/problems/delete-middle-of-linked-list/1/?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''

    # code here
    siz = 0
    cur = head

    while cur:
        cur = cur.next
        siz += 1

    cur = head
    pre = head
    pos = 0

    while cur:
        if siz & 1 and pos == siz // 2:
            pre.next = pre.next.next
            return head
        elif not siz & 1 and pos == siz // 2:
            pre.next = pre.next.next
            return head
        pre = cur
        cur = cur.next
        pos += 1

    # TC: O(N); SC: O(1)