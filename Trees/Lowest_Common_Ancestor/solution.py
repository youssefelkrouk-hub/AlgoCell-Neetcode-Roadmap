# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p == root or q == root : 
            return root 
        elif p == q : 
            return p 
        else :
            curr = root 
            while curr : 
                if p.val > curr.val and q.val > curr.val :
                    curr = curr.right 
                elif p.val < curr.val and q.val < curr.val : 
                    curr = curr.left 
                else :
                    return curr 
        return None
        