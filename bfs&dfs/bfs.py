class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
    def __str__(self):
        return "Node("+str(self.value) +")"

#i will use a queue becuase it support the FIFO operations : the first node  and it's children that i will visit i will append it to the queue 

def bfs(node,queue):
    queue.append(node)
    while len(queue)>0:
        node=queue.pop(0)
        if node is not None:
            print(node)
            queue.append(node.left)
            queue.append(node.right)

mytree=Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
bfs(mytree,[])