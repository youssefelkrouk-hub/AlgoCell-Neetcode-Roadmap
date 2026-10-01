import java.util.HashSet;
import java.util.Set;

public class solution1 {
    static int sumSquare(int n) {
        int output = 0;
        while (n != 0) {
            int digit = n % 10;
            output += digit * digit;
            n /= 10;
        }
        return output;
    }

    static boolean isHappyNumber(int n) {
        Set<Integer> seen = new HashSet<>();
        while (!seen.contains(n)) {
            seen.add(n);
            n = sumSquare(n);
            if (n == 1) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isHappyNumber(19)); // true
        System.out.println(isHappyNumber(2));  // false
    }
}