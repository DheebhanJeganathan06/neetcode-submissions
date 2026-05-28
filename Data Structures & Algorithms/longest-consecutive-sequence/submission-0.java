class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int num : nums) {
            set.add(num);
        }

        int longest = 0;

        for(int curr : set) {
            if(!set.contains(curr - 1)) {
                int length = 1;
                while(set.contains(curr + length)) {
                    length++;
                }

                longest = (length > longest) ? length : longest;
            }
        }

        return longest;
    }
}
