# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        rs = [ ]
        if not root : 
            return rs 
        q = [root] 
        while q : 
            l = len( q ) 
            curr = []
            for _ in range(l) :
                node = q.pop(0) 
                curr.append( node.val )
                if node.left : 
                    q.append( node.left ) 
                if node.right : 
                    q.append( node.right )
            rs.append( curr )

        return rs 