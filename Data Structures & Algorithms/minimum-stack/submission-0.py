class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # to store min values, top stores current minimum

    def push(self, val: int) -> None:
        self.stack.append(val)
        #update minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        removed = self.stack.pop()
        #remove corresponding min entry
        if self.minStack[-1] == removed:
            self.minStack.pop()


    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
