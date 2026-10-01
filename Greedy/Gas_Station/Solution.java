class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length ; 
        long fl = 0 ; 
        for( int i=0 ; i<n ; ++i ){
            fl += ( gas[i] - cost[i] ) ; 
        }
        if( fl < 0 ) return -1 ; 
        long prefix = 0 ; 
        int rs = 0; 
        for( int i=0 ; i<n ; ++i ){
            prefix += ( gas[i] - cost[i] ) ; 
            if( prefix < 0 ) {
                prefix = 0 ; 
                rs = i+1  ;
            }
        }
        return rs ; 
    }
}