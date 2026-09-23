class Solution(object):
    def search(self, nums, target):
        n = len( nums )
        l = 0 
        r = n-1 
        while l < r : 
            mid = l + ( r-l )//2 
            if nums[r] > nums[mid] : 
                r = mid  
            else : 
                l = mid + 1 
        r = l + n-1 
        while l < r : 
            mid = l + ( r - l )//2 
            if nums[mid%n] > target : 
                r = mid - 1 
            elif nums[mid%n] < target : 
                l = mid + 1 
            else : 
                return mid%n

        l %= n 
        if nums[l] == target : 
            return l 
        return -1 
        