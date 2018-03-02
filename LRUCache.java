


http://sophiafeng.com/2013/11/21/lru-cache-implementation-by-linkedhashmap-leetcode/
https://github.com/nagajyothi/InterviewBit/blob/master/HeapsAndMaps/LRU.java


public class LRUCache {
    private int capacity;
    // private TreeMap<Integer, Integer> map;
    final LinkedHashMap<Integer, Integer> map = new LinkedHashMap<Integer, Integer>() {
        @Override
        protected boolean removeEldestEntry(final Map.Entry eldest) {
            return size() > capacity;
            
        }
    };
    public Solution(int capacity) {
        this.capacity = capacity;
    }
    
    /* In Get operation also, key needs to be updated as fresh. so thats why we will remove it first and then put it fresh to cehnage it eldest property*/
    public int get(int key) {
        if(map == null || map.get(key) == null) return -1;
        int value = map.get(key);
        map.remove(key);
        map.put(key, value);
        return value;
    }
    
    /* In put also, if key is availble we are first changing it by geting it and then updating again*/    
    public void set(int key, int value) {
        if(map == null) return;
        get(key);
        map.put(key, value);
    }
}











