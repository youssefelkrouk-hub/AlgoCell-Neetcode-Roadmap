class Solution {
    public:
        int n , m ; 
        int dfs( vector<vector<int>> &g , int i , int j ){
            g[i][j] = 0 ; 
            int rs = 1 ; 
            if(i+1<n&&g[i+1][j]==1) rs += dfs(g,i+1,j) ;
            if(j+1<m&&g[i][j+1]==1) rs += dfs(g,i,j+1) ;
            if(i>0&&g[i-1][j]==1) rs += dfs(g,i-1,j) ;
            if(j>0&&g[i][j-1]==1) rs += dfs(g,i,j-1) ;
            return rs ; 
        }
        int maxAreaOfIsland(vector<vector<int>>& grid) {
            n = grid.size() ; 
            m = grid[0].size() ; 
            int rs = 0 ; 
            for( int i=0 ; i<n ; ++i ){
                for( int j=0 ; j<m ; ++j ){
                    if( grid[i][j] == 1 ) {
                        rs = max( rs , dfs( grid , i, j ) ) ; 
                    }
                }
            }
            return rs ; 
        }
    };