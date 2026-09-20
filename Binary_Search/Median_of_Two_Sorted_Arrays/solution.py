class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2): 
            n = len( nums1 ) 
            m = len( nums2 )
            if n + m == 0 : 
                return 0
            if n > m : 
                return self.findMedianSortedArrays( nums2 , nums1 ) 
            length = ( n+m+1 )//2
            l = 0 ; 
            r = n ;  
            while l <= r : 
                part1 = l + ( r - l )//2 
                part2 = length - part1 

                max1 = nums1[part1-1] if part1 > 0 else -float('inf')
                max2 = nums2[part2-1] if part2 > 0 else -float('inf')
                maxLeft = max( max1 , max2 )

                min1 = nums1[part1] if part1 < n  else float('inf')
                min2 = nums2[part2] if part2 < m  else float('inf')
                minRight = min( min1 , min2 )

                if maxLeft <= minRight : 
                    if ( n + m ) % 2 == 0 : 
                        return ( float(maxLeft) + minRight )/2 
                    else : 
                        return float(maxLeft) 
                elif max1 > min2 : 
                    r = part1 -1 
                else : 
                    l = part1 +1

