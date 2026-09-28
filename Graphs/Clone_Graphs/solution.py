
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional, List


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        q: List["Node"] = [node]
        m = {node: Node(node.val)}
        while q:
            curr = q.pop()
            for nei in curr.neighbors:
                if nei not in m:
                    m[nei] = Node(nei.val)
                    q.append(nei)
                m[curr].neighbors.append(m[nei])

        return m[node]
