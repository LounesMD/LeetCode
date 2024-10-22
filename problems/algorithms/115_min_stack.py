class MinStack:

    def __init__(self):
        self.root = [] # All elements stores the min element       

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or min_val > val: # In case val is the new min 
            min_val = val
        self.root.append([val, min_val])

    def pop(self) -> None:
        self.root.pop()

    def top(self) -> int:
        return self.root[-1][0] if (len(self.root) > 0) else None 

    def getMin(self) -> int:
        return self.root[-1][1] if (len(self.root) > 0) else None 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()