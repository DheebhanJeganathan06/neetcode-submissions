class Solution {
    public int longestConsecutive(int[] nums) {
        List<Integer> starters = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        int longest = 0;

        for(int i : nums) {
            set.add(i);
        }

        for(int i : set) {
            if(!set.contains(i - 1)) {
                int currLength = 1;
                while(set.contains(++i)) {
                    currLength++;
                }
                longest = Math.max(longest, currLength);
            }
        }

        return longest;
    }
}