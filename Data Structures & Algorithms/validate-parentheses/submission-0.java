class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char curr = ' ';
        for(int i = 0; i < s.length(); i++) {
            curr = s.charAt(i);

            if(curr == ')') {
                if(stack.isEmpty() || stack.pop() != '(') {
                    return false;
                }
            }
            else if(curr == ']') {
                if(stack.isEmpty() || stack.pop() != '[') {
                    return false;
                }
            }
            else if(curr == '}') {
                if(stack.isEmpty() || stack.pop() != '{') {
                    return false;
                }
            }
            else {
                stack.push(curr);
            }
        }

        return stack.isEmpty();
    }
}