package Two_Pointers.Happy_Number_;

public class Solution {
    private int sumSquare(int n) {
        int output = 0;
        while (n != 0) {
            int digit = n % 10;
            output += digit * digit;  // note: squares the digit
            n /= 10;
        }
        return output;
    }

    public boolean isHappy(int n) {
        int slow = n, fast = sumSquare(n);
        while (slow != fast) {
            slow = sumSquare(slow);
            fast = sumSquare(sumSquare(fast));
        }
        return fast == 1;
    }
} {
    
}
