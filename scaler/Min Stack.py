class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        # stack = []
        # minStack = []
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return
        temp = self.stack.pop()
        if temp == self.minStack[-1]:
            self.minStack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.minStack) == 0:
            return -1
        return self.minStack[-1]

# clean

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minstack or x < self.minstack[-1]:
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            p = self.stack.pop()
        if self.minstack and p == self.minstack[-1]:
            self.minstack.pop()

    # @return an integer
    def top(self):
        if not self.stack:
            return -1

        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if not self.minstack:
            return -1

        return self.minstack[-1]

    # TC: O(Q); SC: O(N + X)
    # X -> minStack size
    # Q -> Querries 