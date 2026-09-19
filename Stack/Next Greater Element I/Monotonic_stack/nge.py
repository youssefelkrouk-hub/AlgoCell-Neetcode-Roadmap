print("\n")

def monotonic_decreasing_stack(nums):
    stack = []
    for num in nums:
        # Maintain decreasing order: pop elements <= current num
        while stack and stack[-1] <= num:
            stack.pop()
        stack.append(num)
    return stack

nums=[1,2,3,4]
print(monotonic_decreasing_stack(nums))
# we use this monotonic decreasing stack to implemente the next greater element 

print("\n")

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

print("let's implement the Next Smaller Elment usign a Monotonic increasing stack: ")

# the code of an increasing stack : 



def nse(nums):
    n=len(nums)
    stack=[]
    res=[0]*(len(nums))
    for i in range(n-1,-1,-1):
        while stack and stack[-1]>=nums[i]:
            stack.pop()
        if stack:
            res[i]=stack[-1]
        else:
            res[i]=-1
        stack.append(nums[i])
    return res

print("\n")
nums_2=[1,3,4,2]
print(nse(nums_2)) # -->  [-1,2,2,-1] , time complexity is 




# Another problem if we want to retur a hash map , that map every element in nums2 into their next greater element 

def nge_map(nums):
    hash_map,stack={},[]
    n=len(nums)
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=nums[i]:
            stack.pop()
        hash_map[nums[i]]=-1 if  not stack else stack[-1] # if the stack is empty we add -1, else we add the top elemnt wich is exactly the next greater element of nums[i] 
        stack.append(nums[i])

    return hash_map



L=[1,3,4,2]  
print(nge_map(L))

# nums1 is a subset of nums2 , serachin for the next alment of all elment of nums1 in nums2

## Time Complexity: O(n + m) –---    one pass over nums2 and nums1.
## Space Complexity: O(n)    –---    stack and nextGreater array. 

def nge_problem(nums1,nums2):
    hash_map,stack={},[]
    for i in range(len(nums2)-1,-1,-1):
        while stack and stack[-1]<=nums2[i]:
            stack.pop()
        hash_map[nums2[i]]=-1 if not stack else stack[-1]
        stack.append(nums2[i])
    return [hash_map[num] for num in nums1] 

L1 = [4,1,2]
L2 = [1,5,4,2,8]
print(nge_problem(L1,L2))
    