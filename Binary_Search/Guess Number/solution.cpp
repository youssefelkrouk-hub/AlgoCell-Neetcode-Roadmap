/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return       -1 if num is higher than the picked number
 *                1 if num is lower than the picked number
 *                otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long left = 1, right = n;  // use long to avoid overflow when n is close to INT_MAX
        while (left <= right) {
            long mid = left + (right - left) / 2;
            int result = guess((int)mid);
            if (result < 0) {
                right = mid - 1;
            } else if (result > 0) {
                left = mid + 1;
            } else {
                return (int)mid;
            }
        }
        return -1; // not reached under problem constraints, but keeps the function well-formed
    }
};