# question --> https://practice.geeksforgeeks.org/problems/find-the-sum-of-last-n-nodes-of-the-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


def sumOfLastN_Nodes(head, n):
    # function should return sum of last n nodes

    siz = 0
    cur = head

    while cur:
        siz += 1
        cur = cur.next

    p = siz - n

    summ = 0
    i = 1
    cur = head
    while cur:
        if i > p:
            summ += cur.data

        cur = cur.next
        i += 1

    return summ 