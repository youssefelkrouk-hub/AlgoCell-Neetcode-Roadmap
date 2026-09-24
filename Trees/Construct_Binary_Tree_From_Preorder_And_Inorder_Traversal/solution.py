# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.i = 0
        self.p = 0
    def buildTree(self, preorder, inorder):
        def helper(val):
            if self.p >= len(preorder):
                return None
            if inorder[self.i] == val:
                self.i += 1
                return None
            root = TreeNode(preorder[self.p])
            self.p += 1
            root.left = helper(root.val)
            root.right = helper(val)
            return root
        return helper(float('-inf'))