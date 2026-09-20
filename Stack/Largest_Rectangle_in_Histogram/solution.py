class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        rs = 0
        left = [0]*n
        right = [0]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = i - stack[-1] 
            else:
                left[i] = i+1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - i 
            else:
                right[i] = n-i  
            stack.append(i) 

        for i in range(n):
            rs = max(rs, (left[i] + right[i] - 1) * heights[i])

        return rs
