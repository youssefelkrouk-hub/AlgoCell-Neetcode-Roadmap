#include <cctype>
#include <string>

class Solution {
public:
    bool isPalindrome(std::string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (!isalnum(s[left])) {
                left++;
            } else if (!isalnum(s[right])) {
                right--;
            } else if (tolower(s[left]) != tolower(s[right])) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
};