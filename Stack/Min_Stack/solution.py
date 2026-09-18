class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack: # if the min_stack is empty we add val as the first current min
            self.min_stack.append(val)
        else: # compare with the last min  i min_stack
            t=min(self.min_stack[-1],val)
            self.min_stack.append(t)

    def pop(self):
        if not self.min_stack:
            return 0
        self.stack.pop()
        self.min_stack.pop() # pop  from both , they must stay sync

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1] # current min always sitting at the top
 
