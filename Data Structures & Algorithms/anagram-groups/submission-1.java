class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for(String str : strs) {
            int[] arr = new int[26];
            for(Character c : str.toCharArray()) {
                arr[c - 'a']++;
            }

            map.putIfAbsent(Arrays.toString(arr), new ArrayList<String>());
            map.get(Arrays.toString(arr)).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
