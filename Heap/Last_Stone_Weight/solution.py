class Solution(object):
    def lastStoneWeight(self, stones):
        maxStone = max( stones ) 
        curr = len( stones ) 
        f = [0]*(maxStone+1) 
        for stone in stones : 
            f[stone] += 1 
        idx = maxStone
        prev = 0
        while idx > 0 :
            if f[idx] == 0 :
                idx -= 1
                continue 
            elif prev != 0 :
                if idx != prev :
                    ele = prev - idx 
                    if ele <= idx : 
                        f[ele] += 1 
                        prev = 0 
                    else :
                        prev = ele 
                    f[idx] -= 1 
                else : 
                    prev = 0
                    f[idx] -= 1 
            else :
                if f[idx] % 2 != 0 :
                    prev = idx 
                idx -= 1 
            

        return prev
