class Solution(object):
    def findMin(self, nums):
        n = len( nums )
        if n == 1 : 
            return nums[0] 
        l = 1  
        r = n-1 
        while l < r : 
            mid = l + ( r - l )//2 
            if nums[mid] > nums[0] : 
                l = mid + 1 
            else : 
                r = mid
        if nums[l] < nums[0] : 
            return nums[l] 
        return nums[0] 
