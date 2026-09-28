class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        ans = nums[0]
        prefix = 0
        suffix = 0
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            ans = max(ans, max(prefix, suffix))
        return ans
