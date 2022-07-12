head = None
size = 0

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    global head
    global size
    if position >= 1 and position <= size + 1:
        newNode = Node(value)
        if position == 1:
            newNode.next = head
            head = newNode
        else:
            count = 1
            prevNode = head
            while count < position - 1:
                prevNode = prevNode.next
                count += 1
            newNode.next = prevNode.next
            prevNode.next = newNode
        size += 1

def delete_node(position):
    # @param position, integer
    # @return an integer
    global head
    global size
    if position >= 1 and position <= size:
        delNode = None
        if position == 1:
            delNode = head
            head = head.next
        else:
            count = 1
            prevNode = head
            while count < position - 1:
                prevNode = prevNode.next
                count += 1
            delNode = prevNode.next
            prevNode.next = prevNode.next.next
        size -= 1

def print_ll():
    # Output each element followed by a space
    global head
    printVal = head
    ans = list()
    while printVal:
        ans.append(str(printVal.val))
        printVal = printVal.next
    print(' '.join(ans))

# alternative approach

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.head = None
        self.ll_len = 0

    def __repr__(self):
        n = self.head
        nodes = []
        while n:
            nodes.append(str(n.val))
            n = n.next
        return ' '.join(nodes)

    def __get_node(self, index):
        if index == 0:
            return None, self.head
        else:
            prev = None
            cur = self.head
            while index > 0:
                prev = cur
                cur = cur.next
                index -= 1
            return prev, cur

    def insert_at(self, index, val):
        if index > self.ll_len:
            return
        p, c = self.__get_node(index)
        if not p and not c:
            self.head = ListNode(val)
        else:
            new = ListNode(val)
            if not p:
                new.next = c
                self.head = new
            else:
                temp = p.next
                p.next = new
                new.next = temp
        self.ll_len += 1

    def delete_at(self, index):
        if index >= self.ll_len:
            return
        else:
            dummy = prev = ListNode(0)
            prev.next = self.head
            cur = self.head
            while index:
                prev = cur
                cur = cur.next
                index -= 1
            prev.next = cur.next
            self.head = dummy.next
            self.ll_len -= 1


ll = LinkedList()


def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    ll.insert_at(position - 1, value)


def delete_node(position):
    # @param position, integer
    # @return an integer
    ll.delete_at(position - 1)


def print_ll():
    # Output each element followed by a space
    print(ll.__repr__())

# elegant

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head, size):
        self.head = head
        self.size = size


ll = LinkedList(None, 0)


def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    node = Node(value)

    if position == 1:
        node.next = ll.head
        ll.head = node

    elif position <= ll.size + 1:
        tail = ll.head
        i = 1
        while i < position - 1:
            tail = tail.next
            i += 1
        node.next = tail.next
        tail.next = node

    else:
        return

    ll.size += 1


def delete_node(position):
    # @param position, integer
    # @return an integer
    if ll.head and position == 1:
        ll.head = ll.head.next

    elif position <= ll.size:
        tail = ll.head
        i = 1
        while i < position - 1:
            tail = tail.next
            i += 1
        tail.next = tail.next.next

    else:
        return

    ll.size -= 1


def print_ll():
    # Output each element followed by a space
    cur = ll.head
    if not cur:
        return

    n = ll.size
    while cur.next:
        print(cur.val, end=' ')
        cur = cur.next

    # printing the last statement
    print(cur.val, end='')
    print()

# TC: O(N); SC: O(1)