class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = heights[0];
        Stack<int[]> stack = new Stack<>();

        for(int i = 0; i < heights.length; i++) {
            int l = i;
            while(!stack.isEmpty() && stack.peek()[0] > heights[i]) {
                int[] curr = stack.pop();
                maxArea = Math.max(maxArea, curr[0] * (i - curr[1]));
                l = curr[1];
            }
            stack.push(new int[]{heights[i], l});
        }

        while(!stack.isEmpty()) {
            int[] curr = stack.pop();
            maxArea = Math.max(maxArea, curr[0] * (heights.length - curr[1]));
        }
        
        return maxArea;
    }
}