# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def mid(self, A):
        if not A: return

        slow, fast = A, A

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow


    def mergeSort(self, A):
        if not A or not A.next:
            return A

        mid = self.mid(A)

        res = mid.next
        mid.next = None

        l = self.mergeSort(A)
        r = self.mergeSort(res)

        return self.merge(l, r)


    def merge(self, l1, l2):
        c1 = l1
        c2 = l2

        dummy = ListNode(0)

        temp = dummy

        while c1 and c2:
            if c1.val < c2.val:
                temp.next = c1
                c1 = c1.next
                temp = temp.next
            else:
                temp.next = c2
                c2 = c2.next
                temp = temp.next

        while c1:
            temp.next = c1
            c1 = c1.next
            temp = temp.next

        while c2:
            temp.next = c2
            c2 = c2.next
            temp = temp.next

        return dummy.next


    def sortList(self, A):
        return self.mergeSort(A)

    # TC: O(NlogN); SC: O(logN)