class MinStack:
    def __init__(self):
        self.stack = []
        self.head = -1
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.head +=1

        if(self.min == None or val <= self.min):
            self.min = val

    def pop(self) -> None:
        x= self.stack.pop()
        self.head -=1
        if(x == self.min):
            if(len(self.stack) != 0):
                self.min = min(self.stack)
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[self.head]
        

    def getMin(self) -> int:
        return self.min
        
