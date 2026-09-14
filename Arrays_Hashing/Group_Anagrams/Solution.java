import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> strMap = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String s = new String(chars);

            if (!strMap.containsKey(s)) {
                List<String> list = new ArrayList<>();
                list.add(str);
                strMap.put(s, list);
            } else {
                strMap.get(s).add(str);
            }
        }

        return new ArrayList<>(strMap.values());
    }
}