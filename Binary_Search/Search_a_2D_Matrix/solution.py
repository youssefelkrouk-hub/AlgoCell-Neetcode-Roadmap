class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix) 
        m = len(matrix[0])
        l = 0  
        r = n*m - 1 
        while l < r : 
            mid = l + ( r - l )//2 
            row = mid // m 
            col = mid % m 
            if matrix[row][col] > target : 
                r = mid - 1 
            elif matrix[row][col] < target :  
                l = mid + 1 
            else : 
                return True 

        return matrix[l//m][l%m] == target