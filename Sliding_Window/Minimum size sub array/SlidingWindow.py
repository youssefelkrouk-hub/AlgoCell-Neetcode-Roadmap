class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum=sum(nums[:k])
        max_sum=current_sum
        d=k-1
        g=0

        while d < len(nums) - 1:
            current_sum+=nums[d+1]-nums[g]
            max_sum=max(max_sum,current_sum)
            g+=1
            d+=1
        return max_sum/k
            
        
        