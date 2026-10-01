class Solution(object):
    def jump(self, nums):
        n = len(nums) 
        if n == 1 : 
            return 0 
        next = 0  
        limit = nums[0] 
        rs = 1 
        for i in range(n) :
            if i <= limit : 
                if i + nums[i] > next :
                    next = i + nums[i] 
            else :
                rs += 1
                limit = next 
                next = i + nums[i]
        return rs  