class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for(String tok : tokens) {
            if(tok.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            }
            else if (tok.equals("-")) {
                stack.push((stack.pop() - stack.pop()) * -1);
            }
            else if (tok.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            }
            else if (tok.equals("/")) {
                int first = stack.pop();
                int second = stack.pop();
                stack.push(second / first);
            }
            else {
                stack.push(Integer.parseInt(tok));
            }
        }

        return stack.pop();
    }
}