class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if( text1.length() < text2.length() ){
            String temp = text1 ; 
            text1 = text2 ; 
            text2 = temp ;
        }
        int n = text1.length() ; 
        int m = text2.length() ; 
        int[] dp = new int[m+1] ; 
        for( int i=n-1 ; i>=0 ; --i ){
            int next = 0 ; 
            for( int j=m-1 ; j>=0 ; --j ){
                int temp = dp[j] ; 
                if( text2.charAt(j) == text1.charAt(i) ){
                    dp[j] = 1 + next ; 
                }else {
                    dp[j] = Math.max( dp[j] , dp[j+1] ) ;  
                }
                next = temp ; 
            }
        }
        return dp[0] ; 
    }
}