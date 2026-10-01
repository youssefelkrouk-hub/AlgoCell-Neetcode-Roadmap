class Solution {
public:
    string multiply(string num1, string num2) {
        int n = num1.size() ; 
        int m = num2.size() ; 
        vector<int> count( n + m , 0 ) ; 
        for( int i=0 ; i<n ; ++i ){
            int a = (num1[n-1-i] - '0') ; 
            for( int j=0 ; j<m ; ++j ){
                int b = (num2[m-1-j] - '0') ; 
                count[i+j] += a*b ; 
            }
        }
        int c = 0 ;
        for( int i=0 ; i<n+m ; ++i ){
            count[i] += c ; 
            c = count[i] / 10 ; 
            count[i] %= 10 ; 
        }
        string ans ; 
        int l = n+m-1 ; 
        while( l > 0 && count[l] == 0 ) l-- ; 
        while( l >= 0 ){
            ans.push_back( count[l] + '0' ) ; 
            l-- ;
        }
        return ans ; 
    }
};