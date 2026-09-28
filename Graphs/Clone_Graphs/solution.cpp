class Solution {
    public:
        Node* cloneGraph(Node* node) {
            if (!node) return nullptr;
    
            map<Node*, Node*> m;
            queue<Node*> q;
    
            m[node] = new Node(node->val);
            q.push(node);
    
            while (!q.empty()) {
                Node* curr = q.front();
                q.pop();
    
                for (Node* nei : curr->neighbors) { 
                    if (m.find(nei) == m.end()) {   
                        m[nei] = new Node(nei->val);
                        q.push(nei);
                    }
                    m[curr]->neighbors.push_back(m[nei]);
                }
            }
    
            return m[node];
        }
    };
    