import java.util.* ; 
class Solution {
    int n , m ; 
    public void dfs( char[][] grid , int i , int j ){
        grid[i][j] = '0' ;
        if( i+1<n && grid[i+1][j] == '1' ) dfs( grid,i+1,j );
        if( j+1<m && grid[i][j+1] == '1' ) dfs( grid,i,j+1);
        if( i-1>=0 && grid[i-1][j] == '1' ) dfs( grid,i-1,j);
        if( j-1>=0 && grid[i][j-1] == '1' ) dfs( grid,i,j-1);
    }
    public int numIslands(char[][] grid) {
        this.n = grid.length ; 
        this.m = grid[0].length ; 
        int rs = 0; 
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
}