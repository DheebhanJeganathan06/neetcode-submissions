class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set <Integer> set = new HashSet<>(); // initialize hashet used to track duplicates
        
        for(int i : nums) { // can use for each loop since we don't need to track indices
            if(set.contains(i)) {
                return true; // returns true if the current 'i' value in nums has already been tracked by set
            }
            set.add(i); // each iteration of nums, the current 'i' value is added to set to track duplicates later
        }

        return false; // false is returned if nums has been fully traversed without a duplicate being tracked
    }
}
