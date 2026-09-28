class Solution {
    int n , m ; 
    int dfs( int[][] grid , int i , int j ){
        grid[i][j] = 0 ; 
        int rs = 1 ; 
        if(i+1<n && grid[i+1][j]==1 ) rs+=dfs(grid,i+1,j) ; 
        if(j+1<m && grid[i][j+1]==1 ) rs+=dfs(grid,i,j+1) ; 
        if(i>0 && grid[i-1][j]==1 ) rs+=dfs(grid,i-1,j) ; 
        if(j>0 && grid[i][j-1]==1 ) rs+=dfs(grid,i,j-1)  ;
        return rs ; 
    }
    public int maxAreaOfIsland(int[][] grid) {
        this.n = grid.length ; 
        this.m = grid[0].length ; 
        int rs = 0; 
        for( int i=0 ; i<n ; ++i ){
            for( int j=0 ; j<m ; ++j ){
                if( grid[i][j] == 1 ){
                    rs = Math.max( rs , dfs( grid ,i , j ) ) ; 
                }
            }
        }
        return rs ; 
    }
}