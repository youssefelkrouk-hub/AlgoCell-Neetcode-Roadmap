class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> numsIndex1 = new HashMap<>();
        for (int i = 0; i < nums1.length; i++) {
            numsIndex1.put(nums1[i], i);
        }

        int[] res = new int[nums1.length];
        Arrays.fill(res, -1);
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < nums2.length; i++) {
            int curr = nums2[i];
            while (!stack.isEmpty() && curr > stack.peek()) {
                int val = stack.pop();
                int idx = numsIndex1.get(val);
                res[idx] = curr;
            }
            if (numsIndex1.containsKey(curr)) {
                stack.push(curr);
            }
        }

        return res;
    }
}