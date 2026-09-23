# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        else:
            node_map = {} 
            prev = head
            rs = Node(prev.val)
            curr = rs
            node_map[head] = rs
            prev = prev.next

            while prev is not None:
                curr.next = Node(prev.val)
                curr = curr.next
                node_map[prev] = curr
                prev = prev.next

            curr = rs
            prev = head
            while prev is not None:
                if prev.random is not None:
                    curr.random = node_map[prev.random]
                prev = prev.next
                curr = curr.next

            return rs
