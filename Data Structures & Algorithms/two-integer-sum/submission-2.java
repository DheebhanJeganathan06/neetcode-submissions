class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++) {
            if(map.containsKey(target - nums[i])) {
                int val = map.get(target - nums[i]);
                if(val != i) {
                    return new int[]{i, val};
                }
            }
        }

        return new int[0];
    }
}
