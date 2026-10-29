class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min==[]:
            self.min.append(len(self.stack)-1)
        else :
            if val<self.stack[self.min[-1]]:
                self.min.append(len(self.stack)-1)
            else:
                self.min.append(self.min[-1])
    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min[-1]]
