class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
    def __str__(self):
        return "Node("+str(self.value) +")"