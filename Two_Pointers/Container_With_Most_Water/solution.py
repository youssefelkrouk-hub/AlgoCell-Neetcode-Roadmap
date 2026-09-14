class Solution:
    def maxArea(self, height):
        """
        Container With Most Water - two pointer approach.
        Time: O(n), Space: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            shorter = min(height[left], height[right])
            max_area = max(max_area, width * shorter)

            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area