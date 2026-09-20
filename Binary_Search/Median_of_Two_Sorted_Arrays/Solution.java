class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
       int n = nums1.length ; 
       int m = nums2.length ; 
       if( n > m ){
            return findMedianSortedArrays( nums2 , nums1 ) ; 
       }
       int len = ( n+m+1 )/2 ;
       int l = 0 ; 
       int r = n ;  
       while( l <= r ){
            int part1 = l + ( r - l )/2 ; 
            int part2 = len - part1 ; 

            int max1 = part1 > 0 ? nums1[part1-1] : Integer.MIN_VALUE ;
            int max2 = part2 > 0 ? nums2[part2-1] : Integer.MIN_VALUE ;
            int maxLeft = Math.max( max1 , max2 ) ;   

            int min1 = part1 < n ? nums1[part1] : Integer.MAX_VALUE ; 
            int min2 = part2 < m ? nums2[part2] : Integer.MAX_VALUE ; 
            int minRight = Math.min( min1 , min2 ) ; 

            if( maxLeft <= minRight ){
                if( (n+m) % 2 == 0 ){
                    return ( maxLeft + minRight ) / 2.0 ; 
                }else {
                    return maxLeft ; 
                }
            }else if( max1 > min2 ){
                r = part1 - 1 ;
            }else {
                l = part1 + 1 ; 
            }
       }
       return 0.0 ;    
}
}