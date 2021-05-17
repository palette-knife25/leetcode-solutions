#  https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)

    def pop(self) -> None:
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.vals[self.vals.index(min(self.vals))]

#####################################################################
obj = MinStack()
obj.push(2)
obj.push(1)
obj.push(3)
obj.push(5)

obj.pop()

param_3 = obj.top()
print(param_3)

param_4 = obj.getMin()
print(param_4)