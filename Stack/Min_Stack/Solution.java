import java.util.Stack;

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty()) { // if the minStack is empty we add val as the first current min
            minStack.push(val);
        } else { // compare with the last min in minStack
            int t = Math.min(minStack.peek(), val);
            minStack.push(t);
        }
    }

    public void pop() {
        if (minStack.isEmpty()) {
            return;
        }
        stack.pop();
        minStack.pop(); // pop from both, they must stay sync
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek(); // current min always sitting at the top
    }
}