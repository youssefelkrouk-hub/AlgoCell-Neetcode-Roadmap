package Sliding_Window.Sliding_Window_Maximum;

import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        Deque<Integer> deq = new ArrayDeque<>();
        int[] rs = new int[n - k + 1];
        for (int i = 0; i < n; i++) {
            while (!deq.isEmpty() && nums[deq.getLast()] <= nums[i]) {
                deq.removeLast();
            }
            if (!deq.isEmpty() && deq.getFirst() <= i - k) {
                deq.removeFirst();
            }
            deq.addLast(i);
            if (i >= k - 1) {
                rs[i - k + 1] = nums[deq.getFirst()];
            }
        }
        return rs ;
    }
}
