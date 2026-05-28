class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arr = new int[nums.length];
        arr[0] = 1;
        for(int i = 1; i < arr.length; i++) {
            arr[i] = arr[i - 1] * nums[i - 1];
        }

        int factor = nums[nums.length - 1];
        for(int i = arr.length - 2; i >= 0; i--) {
            arr[i] *= factor;
            factor *= nums[i];
        }
        
        return arr;
    }
}