class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.mainStack:
            if self.mainStack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1] if self.mainStack else None

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None
