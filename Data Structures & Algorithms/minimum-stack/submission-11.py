import math
class MinStack:

    def __init__(self):
        self.min = (math.inf,None) 
        self.stack = []
        self.top_index = -1
        

    def push(self, val: int) -> None:
        self.top_index+=1
        self.stack.append((val,self.min[1]))
        if val < self.min[0]:    
            self.min = (val,self.top_index) 
        

    def pop(self) -> None:
        
        if self.top_index == self.min[1]:
            top = self.stack[-1]
            # print(top)
            # # print(self.stack[top[1]][0])
            # print(self.stack)
            # print(self.min)

            self.min = (self.stack[top[1]][0] if top[1] != None else math.inf ,top[1])
            print(self.min)
        self.stack.pop()
        self.top_index-=1
        

    def top(self) -> int:
        return self.stack[self.top_index][0]
        

    def getMin(self) -> int:   
        return self.min[0]
        
