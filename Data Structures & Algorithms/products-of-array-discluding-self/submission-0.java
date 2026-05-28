class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        res[0] = 1;
        int tracker = 1;

        for(int i = 1; i < nums.length; i++) {
            res[i] = nums[i - 1] * tracker;
            tracker *= nums[i - 1];
        }

        tracker = nums[nums.length - 1];
        for(int i = nums.length - 2; i >= 0; i--) {
            res[i] *= tracker;
            tracker *= nums[i];
        }

        return res;
    }
}  
