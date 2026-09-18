#include <stack>

class MinStack {
private:
    std::stack<int> stack_;
    std::stack<int> min_stack_;

public:
    MinStack() {}

    void push(int val) {
        stack_.push(val);
        if (min_stack_.empty()) { // if the min_stack is empty we add val as the first current min
            min_stack_.push(val);
        } else { // compare with the last min in min_stack
            int t = std::min(min_stack_.top(), val);
            min_stack_.push(t);
        }
    }

    void pop() {
        if (min_stack_.empty()) {
            return;
        }
        stack_.pop();
        min_stack_.pop(); // pop from both, they must stay sync
    }

    int top() {
        return stack_.top();
    }

    int getMin() {
        return min_stack_.top(); // current min always sitting at the top
    }
};