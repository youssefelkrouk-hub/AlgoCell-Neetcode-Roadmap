


def find_duplicate(nums):
    slow=nums[0]
    fast=nums[0]

    # Step1:

    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break 
    # step2: 
    slow=nums[0]
    while slow!=fast:
        slow=nums[slow]
        fast=nums[fast]
    return slow

L = [1, 3, 4, 2, 2]
print(find_duplicate(L))