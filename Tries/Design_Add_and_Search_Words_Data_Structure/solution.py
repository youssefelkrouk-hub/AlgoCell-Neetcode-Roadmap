class WordDictionary(object):
    def __init__(self):  
        self.childs = [None]*26 
        self.end = False 
    def addWord(self, word):
        root = self 
        for c in word : 
            ind = ord(c) - ord('a') 
            if not root.childs[ind] :
                root.childs[ind] = WordDictionary() 
            root = root.childs[ind]
        root.end = True 

    def search(self, word):
        return self.dfs( self , word , 0 ) 
    def dfs( self , root , word , ind ) : 
        if not root : 
            return False 
        elif ind == len(word) :
            return root.end  
            return False 
        elif word[ind] == '.' :
            for i in range(26) : 
                if root.childs[i] and self.dfs( root.childs[i] , word , ind+1 ):
                    return True 
            return False 
        else : 
            pos = ord( word[ind] ) - ord( 'a' )
            return self.dfs( root.childs[pos] , word , ind+1 )