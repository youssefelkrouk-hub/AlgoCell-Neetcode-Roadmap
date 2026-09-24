#include <string>
#include <vector>

using namespace std;

class Trie {
    Trie* childs[26];
    bool isEnd;
    static int map[128];
    static void initMap() {
        for (char c = 'a'; c <= 'z'; ++c) {
            map[c] = c - 'a';
        }
    }

public:
    Trie() {
        static bool initialized = false;
        if (!initialized) {
            initMap();
            initialized = true;
        }
        for (int i = 0; i < 26; ++i) {
            childs[i] = nullptr;
        }
        isEnd = false;
    }

    void insert(string word) {
        Trie* root = this;
        for (char c : word) {
            int index = map[c];
            if (root->childs[index] == nullptr) {
                root->childs[index] = new Trie();
            }
            root = root->childs[index];
        }
        root->isEnd = true;
    }

    bool search(string word) {
        Trie* root = this;
        for (char c : word) {
            int index = map[c];
            if (root->childs[index] == nullptr) {
                return false;
            }
            root = root->childs[index];
        }
        return root->isEnd;
    }

    bool startsWith(string prefix) {
        Trie* root = this;
        for (char c : prefix) {
            int index = map[c];
            if (root->childs[index] == nullptr) {
                return false;
            }
            root = root->childs[index];
        }
        return true;
    }
};

int Trie::map[128] = {};