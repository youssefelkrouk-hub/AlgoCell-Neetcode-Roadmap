def nge(nums):
    n = len(nums)
    res = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]   # top of stack = next greater element
        else:
            res[i] = -1          # nothing greater found
        stack.append(nums[i])    # push current element for future comparisons
    return res

nums=[1,3,4,2]
print(nge(nums))