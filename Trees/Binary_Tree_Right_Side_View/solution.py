# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        rs = [] 
        if not root : 
            return rs 
        q = [root]
        while q : 
            s = len(q) 
            val = -1   
            for _ in range(s) : 
                curr = q.pop(0)
                val = curr.val 
                if curr.left : 
                    q.append( curr.left )
                if curr.right : 
                    q.append( curr.right )
            rs.append(val)
        return rs 
        