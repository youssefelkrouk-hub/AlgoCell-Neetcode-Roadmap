import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
       List<List<String>> dp = new ArrayList<>() ; 
        for( int i=0 ; i<=n ; ++i ){
            dp.add( new ArrayList<>() ) ; 
        }
        dp.get(0).add( "" ) ; 
        for( int k=1 ; k<=n ; ++k ){
            for( int i=0 ; i<k ; ++i ){
                for( String a : dp.get( i ) ){
                    for( String b : dp.get( k-i-1 ) ){
                        dp.get(k).add( "(" + a + ")" + b  ) ; 
                    }
                }
            }
        }

        return dp.get(n) ; 
    }
}