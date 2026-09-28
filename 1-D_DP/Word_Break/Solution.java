import java.util.* ; 
class Solution {
    public static boolean check( String s , String w , int in ){
        for( int i=in ; i<in+w.length() ; ++i ){
            if( s.charAt(i) != w.charAt(i-in) ){
                return false ; 
            }
        }
        return true ; 
    }
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length() ; 
        boolean[] dp = new boolean[n+1] ; 
        dp[0] = true ; 
        for( int i=0 ; i<n ; ++i ){
            if( dp[i] ){
                for( String w : wordDict ){
                    if( i + w.length() <= n && check( s , w , i )){
                        dp[i+w.length()] = true ; 
                    }
                }
            }
        }
        return dp[n] ; 
    }
}
