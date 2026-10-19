# in this solution i will use an extra memory wich is a list :
def moves_zero(nums):
    left=0
    L=[]
    for right in range(0,len(nums)):
        if nums[right]!=0:
            L.append(nums[right])
            left+=1
    # in this section left is used to track in wich index we stop adding the non-null value
    for i in range(left,len(nums)):
        L.append(0)
    return L

list=[0,1,0,3,12]
print(moves_zero(list))