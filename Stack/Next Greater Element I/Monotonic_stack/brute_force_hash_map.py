class solution:
    def nextGreaterelment(nums1,nums2):
        #O(n*m) 
        nums1Indx={n:i for i,n in enumerate(nums1)}
        res=[-1]*(len(nums1))


        for i in range(len(nums2)):
            if nums2[i] not in nums1Indx: # if  an elment in nums2 that's not in nums1 ,
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    index=nums1Indx[nums2[i]]
                    res[index]=nums2[j]
                    break
        return res



nums1 = [4,1,2]
nums2 = [1,3,4,2]


t=solution.nextGreaterelment(nums1,nums2)
print(t)