# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val) + ",")
                stack.append(node.right)
                stack.append(node.left)
        return ''.join(res)

    def deserialize(self, data):
        self.data = data
        self.n = len(data)
        self.index = 0
        return self._helper()

    def _helper(self):
        if self.index >= self.n or self.data[self.index] == '#':
            return None
        neg = False
        if self.data[self.index] == '-':
            neg = True
            self.index += 1

        val = 0
        while self.index < self.n and self.data[self.index] != ',':
            val = val * 10 + int(self.data[self.index])
            self.index += 1
        self.index += 1 
        node = TreeNode(-val if neg else val)
        node.left = self._helper()
        self.index += 1 
        node.right = self._helper()
        return node
