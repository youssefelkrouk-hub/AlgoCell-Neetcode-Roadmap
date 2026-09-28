class Solution(object):
    def dfs( self, grid , i , j ) : 
        n = len(grid) 
        m = len(grid[0]) 
        rs = 1  
        grid[i][j] = 0 
        if i+1<n and grid[i+1][j] == 1 : 
            rs += self.dfs( grid , i+1 , j ) 
        if j+1<m and grid[i][j+1] == 1 : 
            rs += self.dfs( grid , i , j+1 ) 
        if j>0 and grid[i][j-1] == 1 : 
            rs += self.dfs( grid , i , j-1 ) 
        if i>0 and grid[i-1][j] == 1 : 
            rs += self.dfs( grid , i-1 , j ) 
        return rs 

    def maxAreaOfIsland(self, grid):
        rs = 0  
        for i in range( len(grid) ) : 
            for j in range( len(grid[0]) ) : 
                if grid[i][j] == 1 : 
                    rs = max( rs , self.dfs( grid ,i , j ) )

        return rs 
        