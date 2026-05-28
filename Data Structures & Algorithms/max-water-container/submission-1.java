class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int maxArea = 0;

        while(l < r) {
            int currArea = 0;
            if(height[l] < height[r]) {
                currArea = height[l] * (r - l);
                l++;
            }
            else {
                currArea = height[r] * (r - l);
                r--;
            }

            maxArea = Math.max(maxArea, currArea);
        }

        return maxArea;
    }
}