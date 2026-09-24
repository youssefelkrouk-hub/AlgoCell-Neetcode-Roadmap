class WordDictionary {
    public:
        vector<WordDictionary*> childs;
        bool end;
    
        WordDictionary() {
            this->end = false;
            this->childs = vector<WordDictionary*>(26, nullptr);
        }
    
        void addWord(string word) {
            WordDictionary* node = this;
            for (char c : word) {
                int idx = c - 'a';
                if (!node->childs[idx]) {
                    node->childs[idx] = new WordDictionary();
                }
                node = node->childs[idx];
            }
            node->end = true;
        }
    
        bool search(string word) {
            return dfs(this, word, 0);
        }
    
        bool dfs(WordDictionary* node, string& word, int in) {
            if (!node) return false;
            if (in == word.size()) return node->end;
    
            if (word[in] == '.') {
                for (int i = 0; i < 26; ++i) {
                    if (node->childs[i] && dfs(node->childs[i], word, in + 1)) {
                        return true;
                    }
                }
                return false;
            } else {
                int idx = word[in] - 'a';
                return dfs(node->childs[idx], word, in + 1);
            }
        }
    };
    