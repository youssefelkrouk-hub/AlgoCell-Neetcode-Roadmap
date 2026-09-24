# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        def dfs( root , curr ) :
            if not root : 
                return 0
            res = 0 
            if root.val >= curr : 
                res += 1 
                curr = max( curr , root.val)
            return res + dfs(root.left,curr) + dfs(root.right,curr)
        return dfs( root , root.val )
        