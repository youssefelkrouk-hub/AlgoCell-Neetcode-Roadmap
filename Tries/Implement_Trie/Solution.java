package Tries.Implement_Trie;

class Trie {
    Trie[] childs ; 
    boolean isEnd ; 
    static int[] map = new int[128] ; 
    static {
        for( char c ='a' ; c<='z' ; c += 1 ){
            map[c] = c - 'a' ; 
        }
    }
    public Trie() {
        this.childs = new Trie[26] ; 
        this.isEnd = false ; 
    }
    
    public void insert(String word) {
        Trie root = this ; 
        for( char c : word.toCharArray() ){
            Trie next = root.childs[map[c]] ; 
            if( next == null ){
                root.childs[map[c]] = new Trie() ;
                next = root.childs[map[c]] ; 
            }
            root = next ; 
        }
        root.isEnd = true ; 
    }
    
    public boolean search(String word) {
        Trie root = this ; 
        for( char c : word.toCharArray() ){
            Trie next = root.childs[map[c]] ; 
            if( next == null ){
                return false ; 
            }
            root = next ; 
        }
        return root.isEnd ; 
    }
    
    public boolean startsWith(String prefix) {
        Trie root = this ; 
        for( char c : prefix.toCharArray() ){
            Trie next = root.childs[map[c]] ; 
            if( next == null ){
                return false ; 
            }
            root = next ; 
        }
        return true  ; 
    }
}
