class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = 0  
        for i in intervals : 
            m = max( m , i[1] )
        
        memo = [-1]*(m+1)

        for i in intervals : 
            memo[i[0]] = max( memo[i[0]] , i[1]  )

        ans = [ ]
        i = 0 
        while memo[i] == -1 : 
            i += 1 
        start = -1 
        end = -1
        while i <= m : 
            if i < end : 
                end = max( end , memo[i] ) 
            elif i == end : 
                if memo[i] <= end :
                    ans.append( [start,end] )
                else: 
                    end = max( end , memo[i] )
            else :
                if memo[i] != -1 : 
                    if memo[i] == i :
                        ans.append( [i,i] )
                    else :
                        start = i 
                        end = memo[i]
            i += 1 

        return ans 