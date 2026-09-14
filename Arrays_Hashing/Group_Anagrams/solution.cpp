#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> strMap;

        for (const string& str : strs) {
            string s = str;
            sort(s.begin(), s.end());

            if (strMap.find(s) == strMap.end()) {
                strMap[s] = vector<string>{str};
            } else {
                strMap[s].push_back(str);
            }
        }

        vector<vector<string>> result;
        for (auto& pair : strMap) {
            result.push_back(pair.second);
        }
        return result;
    }
};