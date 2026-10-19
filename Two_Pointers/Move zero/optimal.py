
# i use tow pointers  left and right , left is to track the null values and  right to track non-null values

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(0,len(nums)):
            if nums[right]!=0:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1