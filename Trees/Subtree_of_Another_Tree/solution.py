# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def serialize(self, root):
        if root is None:
            return "$"
        return "#" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def get_ZArray(self, s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]
        return z

    def isSubtree(self, root, subRoot):
        a = self.serialize(root)
        b = self.serialize(subRoot)
        rs = b + "-" + a
        z = self.get_ZArray(rs)
        n = len(b)
        for i in range(n, len(rs)):
            if z[i] == n:
                return True
        return False
