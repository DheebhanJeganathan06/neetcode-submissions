class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for(String str : strs) {
            int[] arr = new int[26];
            for(Character c : str.toCharArray()) {
                arr[c - 'a']++;
            }

            String key = Arrays.toString(arr);

            map.putIfAbsent(key, new ArrayList<String>());
            map.get(key).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
