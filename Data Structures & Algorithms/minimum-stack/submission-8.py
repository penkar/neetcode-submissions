class MinStack:
    def __init__(self):
        # self.min = None;
        self.stack = []
        
    def push(self, val: int) -> None:
        # if self.min == None or val < self.min:
        #     self.min = val
        self.stack.append(val)
        
    def pop(self) -> None:
        return self.stack.pop()
        # if len(self.stack) == 0:
        #     return null
        # v = self.stack.pop()
        # if len(self.stack) == 0:
        #     self.min = None
        #     return v
        # if self.min == v:
        #     self.min = min(self.stack)
        # return v
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        # return self.min
