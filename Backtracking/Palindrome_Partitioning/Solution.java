import java.util.* ; 
class Solution {
    List<String> curr =  new ArrayList<>() ; 
    boolean isPal( String s , int l , int r ){
        while( l < r ){
            if( s.charAt(l) != s.charAt(r) ){
                return false ; 
            }
            l++ ; r--; 
        }
        return true ;
    }
    void helper( List<List<String>> rs , String s , int in ){
        if( in == s.length() ){
            rs.add( new ArrayList<>(curr) ) ;  
            return ; 
        }
        for( int i=in ; i<s.length() ; ++i ){
            if( isPal( s , in , i ) ){
                curr.add( s.substring( in ,i+1 ) ) ; 
                helper( rs , s , i+1 ) ; 
                curr.removeLast() ; 
            }
        }
    }
    public List<List<String>> partition(String s) {
        int n = s.length() ; 
        List<List<String>> rs = new ArrayList<>() ; 
        helper( rs , s , 0 ) ; 
        return rs ; 
    }
}