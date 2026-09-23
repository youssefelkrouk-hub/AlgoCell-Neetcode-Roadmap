class Solution(object):
    def findDuplicate(self, nums):
        for num in nums : 
            idx = abs( num ) - 1 
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1 
        return -1 