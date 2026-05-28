class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while(l <= r && l >= 0 && r <= nums.length - 1) {
            int i = (l + r) / 2;

            if(nums[i] == target) {
                return i;
            }
            else if (nums[i] < target) {
                l = i + 1;
            }
            else {
                r = i - 1;
            }
        }

        return -1;
    }
}