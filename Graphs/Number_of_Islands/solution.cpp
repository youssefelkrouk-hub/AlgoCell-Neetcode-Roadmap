class Solution {
    public:
        int n , m ;
        void dfs( vector<vector<char>> &grid , int i , int j ){
            grid[i][j] = '0' ;
            if( i+1<n && grid[i+1][j] == '1' ) dfs( grid,i+1,j );
            if( j+1<m && grid[i][j+1] == '1' ) dfs( grid,i,j+1);
            if( i-1>=0 && grid[i-1][j] == '1' ) dfs( grid,i-1,j);
            if( j-1>=0 && grid[i][j-1] == '1' ) dfs( grid,i,j-1);
        }
        int numIslands(vector<vector<char>>& grid) {
            n = grid.size() ; 
            m = grid[0].size() ; 
            int rs = 0 ; 
            for( int i=0 ; i<n ; ++i ){
                for( int j=0 ; j<m ; ++j ){
                    if( grid[i][j] == '1' ){
                        rs++ ; 
                        dfs( grid , i , j ) ; 
                    }
                }
            }
            return rs ;
        }
    };