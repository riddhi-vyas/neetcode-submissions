class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # top item will be the most recent min val

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        removed = self.stack.pop()
        if self.min_stack[-1] == removed:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]