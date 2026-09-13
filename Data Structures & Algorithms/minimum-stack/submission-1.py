class MinStack:

    def __init__(self):
        self._stack = list()
        self._minStack = list()
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if (len(self._stack) > 1 and self._minStack[-1] < val):
            keep = self._minStack[-1]
            self._minStack.append(val)
            self._minStack.append(keep)
        else:
            self._minStack.append(val)
            self._minStack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._minStack.pop()
        self._minStack.pop()
        
    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._minStack[-1]
