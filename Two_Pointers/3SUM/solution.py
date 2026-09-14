class Solution(object):
    def threeSum(self, nums):
        n = len(nums) 
        res = [] 
        nums.sort()
        i = 0 
        while i < n :  
            if nums[i] > 0:
                break
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            i += 1 
            
        return res
