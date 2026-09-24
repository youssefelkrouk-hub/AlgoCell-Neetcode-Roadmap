class Trie(object):
    map = [0] * 128
    for c in range(ord('a'), ord('z') + 1):
        map[c] = c - ord('a')

    def __init__(self):
        self.childs = [None] * 26
        self.isEnd = False

    def insert(self, word):
        root = self
        for c in word:
            index = Trie.map[ord(c)]
            if root.childs[index] is None:
                root.childs[index] = Trie()
            root = root.childs[index]
        root.isEnd = True

    def search(self, word):
        root = self
        for c in word:
            index = Trie.map[ord(c)]
            if root.childs[index] is None:
                return False
            root = root.childs[index]
        return root.isEnd

    def startsWith(self, prefix):
        root = self
        for c in prefix:
            index = Trie.map[ord(c)]
            if root.childs[index] is None:
                return False
            root = root.childs[index]
        return True