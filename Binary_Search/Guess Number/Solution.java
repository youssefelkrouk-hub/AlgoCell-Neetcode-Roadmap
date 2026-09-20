/**
 * The guess API is defined in the parent class GuessGame.
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1, right = n;
        while (left <= right) {
            int mid = left + (right - left) / 2; // avoids overflow, matters here since ints are fixed-width
            int result = guess(mid);
            if (result < 0) {
                right = mid - 1;
            } else if (result > 0) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}