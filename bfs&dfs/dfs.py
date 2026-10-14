class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
    def __str__(self):
        return "Node("+str(self.value) +")"

#this first method is a rcursive method that explore the children of each node until the end !
def dfs_recursive(tree):
    if tree is not None:
        print(tree)
        dfs_recursive(tree.left)
        dfs_recursive(tree.right)
# i will use a stack Because a stack is LIFO: the last item you push is the first one you pop.

def dfs(tree,stack):
    stack.append(tree)
    while len(stack)>0:
        node=stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)

mytree=Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))

dfs_recursive(mytree)
