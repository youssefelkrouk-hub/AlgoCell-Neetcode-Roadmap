import java.util.*;

class TimeMap {
    Map<String , ArrayList<Integer> > map ; 
    Map<Integer,String> values ;  
    public TimeMap() {
        map = new HashMap<>() ; 
        values = new HashMap<>() ; 
    }
    
    public void set(String key, String value, int timestamp) {
        if( map.get(key) == null ){
            map.put( key , new ArrayList<>() ) ; 
        }
        map.get(key).add( timestamp ) ; 
        values.put( timestamp , value ) ; 
    }
    
    public String get(String key, int timestamp) {
        ArrayList<Integer> prev = map.get(key) ; 
        if( prev == null ) return "" ; 
        int l = 0 ; 
        int r = prev.size() -1 ; 
        while( l < r ){
            int mid = l + ( r - l + 1 )/2 ; 
            if( prev.get(mid) <= timestamp ){
                l = mid ; 
            }else {
                r = mid -1 ; 
            }
        } 
        if( prev.get(l) <= timestamp ){
            return values.get( prev.get(l) ) ; 
        }
        return "" ; 
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */