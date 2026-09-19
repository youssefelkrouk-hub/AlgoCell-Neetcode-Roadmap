# Time: O(n + m)  where n = len(nums1), m = len(nums2) — building the dict is O(n), 
# and the main loop is O(m) amortized
# (each element pushed/popped at most once, same reasoning as your earlier example)
# Space: O(n) for the stack and for the list  
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        numsIndex1={n:i for i,n in enumerate(nums1)}
        res=[-1]*(len(nums1))
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr>stack[-1]:
                val=stack.pop()
                idx=numsIndex1[val]
                res[idx]=curr
            if curr in numsIndex1:
                stack.append(curr)
        return res
        
        