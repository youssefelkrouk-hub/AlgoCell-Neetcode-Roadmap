class Solution(object):
    def dfs( self , grid , i , j ):
        grid[i][j] = '0'
        if i+1<self.n and grid[i+1][j] == '1' : 
            self.dfs( grid , i+1 , j )
        if j+1<self.m and grid[i][j+1] == '1' : 
            self.dfs( grid , i , j+1 )  
        if i>0 and grid[i-1][j] == '1' : 
            self.dfs( grid , i-1 , j )  
        if j>0 and grid[i][j-1] == '1' : 
            self.dfs( grid , i , j-1 )  

    def numIslands(self, grid):
       self.n = len( grid )
       self.m = len( grid[0] )
       rs = 0 
       for i in range(len(grid)) : 
        for j in range(len(grid[0])) : 
            if grid[i][j] == '1' : 
                rs += 1 
                self.dfs( grid , i , j )

       return rs         