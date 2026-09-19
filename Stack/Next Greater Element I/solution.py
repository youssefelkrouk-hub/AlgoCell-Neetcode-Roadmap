# Time: O(n + m)  where n = len(nums1), m = len(nums2) — building the dict is O(n), 
# and the main loop is O(m) amortized
# (each element pushed/popped at most once, same reasoning as your earlier example)
# Space: O(n) for the stack and for the list  
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hash_map,stack={},[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            hash_map[nums2[i]]=-1 if not stack else stack[-1]
            stack.append(nums2[i])
        return [hash_map[num] for num in nums1] 
        