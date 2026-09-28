class Solution {
    public:
        struct BIT{
            vector<int> bit ; 
            int n ; 
            BIT(int len){
                n = len ; 
                bit.assign( n , 0 ) ; 
            }
            int get( int idx ){
                int rs = 0 ;
                while( idx > 0 ){
                    rs = max( rs , bit[idx] ) ; 
                    idx -= idx & -idx ; 
                }
                return rs ; 
            }
            void update( int idx , int val ){
                while( idx < n ){
                    bit[idx] = max( bit[idx] , val ) ; 
                    idx += idx & -idx ; 
                }
            } 
        };
        int lengthOfLIS(vector<int>& nums) {
            int n = nums.size() ; 
            vector<pair<int,int>> m( n ) ; 
            for( int i=0 ; i<n ; ++i ){
                m[i] = { nums[i] , i } ; 
            }
            sort( m.begin() , m.end() ) ; 
            int curr = 1 ; 
            for( int i=0 ; i<n ; ++i ){
                nums[ m[i].second ] = curr ; 
                while( i+1<n && m[i+1].first == m[i].first ){
                    i++ ; 
                    nums[ m[i].second ] = curr ; 
                }
                curr++ ; 
            }
            BIT bit( curr ) ;
            int lis = 0 ;  
            for( int i=0 ; i<n ; ++i ){
                int l = bit.get( nums[i]-1 ) + 1 ; 
                lis = max( lis , l ) ;
                bit.update( nums[i] , l ) ;  
            }
            return lis ; 
        }
    };