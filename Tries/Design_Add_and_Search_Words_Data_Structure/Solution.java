class WordDictionary {
    WordDictionary[] childs ; 
    boolean end ; 
    public WordDictionary() {
        this.childs = new WordDictionary[26] ; 
        this.end = false ; 
    }
    
    public void addWord(String word) {
        WordDictionary root = this ; 
        for( char c : word.toCharArray() ){
            if( root.childs[ c - 'a' ] == null ){
                root.childs[ c - 'a' ] = new WordDictionary() ; 
            }
            root = root.childs[ c - 'a' ] ; 
        }
        root.end = true ; 
    }
    
    public boolean search(String word) {
        return helperSearch( this , word , 0 ) ;  
    }
    public boolean helperSearch( WordDictionary root , String word , int in ){
        if( in == word.length() ) {
            return root.end ; 
        }else if( word.charAt( in ) == '.' ){
            for( int i=0 ; i<26 ; ++i ){
                if( root.childs[i] != null &&
                    helperSearch( root.childs[i] , word , in+1 )
                 ){
                    return true ; 
                 }
            }
            return false ; 
        }else {
            WordDictionary next = root.childs[ word.charAt(in) - 'a' ] ; 
            if( next == null ) return false ; 
            return helperSearch( next , word , in+1 ) ; 
        }
    }
}
