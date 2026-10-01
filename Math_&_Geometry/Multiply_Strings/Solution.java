class Solution {
    public String multiply(String num1, String num2) {
        int n = num1.length() ; 
        int m = num2.length() ; 
        int[] rs = new int[n+m] ; 
        for( int i=0 ; i<n ; ++i ){
            int a = num1.charAt(n-1-i) - '0' ; 
            for( int j=0 ; j<m ; ++j ){
                int b = num2.charAt(m-1-j) - '0' ;
                rs[i+j] += a*b ;
            }
        } 
        int c = 0 ;   
        for( int i=0 ; i<n+m ; ++i ){
            rs[i] += c ; 
            c = rs[i] / 10 ; 
            rs[i] %= 10 ;
        }
        StringBuilder ans = new StringBuilder() ; 
        int l = n+m-1; 
        while( l>0 && rs[l] == 0 ) l-- ; 
        while( l >= 0 ){
            ans.append( rs[l] ) ; 
            l-- ; 
        }
        return ans.toString() ; 
    }
}