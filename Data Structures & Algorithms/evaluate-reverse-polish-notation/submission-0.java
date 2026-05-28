class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String s : tokens) {
            if(s.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            }
            else if(s.equals("-")) {
                int i = stack.pop();
                int j = stack.pop();
                stack.push(j - i);
            }
            else if(s.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            }
            else if(s.equals("/")) {
                int i = stack.pop();
                int j = stack.pop();
                stack.push(j / i);
            }
            else {
                stack.push(Integer.parseInt(s));
            }
        }

        return stack.pop();
    }
}
