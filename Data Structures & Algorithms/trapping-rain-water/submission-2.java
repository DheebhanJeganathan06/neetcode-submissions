class Solution {
    public int trap(int[] height) {
        int l = 0, r = height.length - 1;
        int totalWater = 0;
        int lMax = height[0], rMax = height[height.length - 1];

        while(l < r) {
            lMax = Math.max(lMax, height[l]);
            rMax = Math.max(rMax, height[r]);
            int h = 0;

            if(lMax < rMax) {
                h = lMax - height[l];
                if(h > 0) {
                    totalWater += h;
                }
                l++;
            }
            else {
                h = rMax - height[r];
                if(h > 0) {
                    totalWater += h;
                }
                r--;
            }
        }

        return totalWater;
    }
}