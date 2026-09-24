package Backtracking.Combination_Sum_II;

import java.util.*;

class Solution {
    public int minCost(int n, int[] cuts) {
        int[] c = new int[cuts.length + 2];
        int m = cuts.length;
        for (int i = 0; i < m; ++i) c[i + 1] = cuts[i];
        c[0] = 0;
        c[m + 1] = n;
        Arrays.sort(c);
        int[][] dp = new int[m + 2][m + 2];
        for (int len = 2; len <= m + 1; ++len) {
            for (int i = 0; i + len <= m + 1; ++i) {
                int j = i + len;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i + 1; k < j; ++k) {
                    dp[i][j] = Math.min(dp[i][j], c[j] - c[i] + dp[i][k] + dp[k][j]);
                }
            }
        }

        return dp[0][m + 1];
    }
}
