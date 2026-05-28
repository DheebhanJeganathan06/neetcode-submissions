class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] arr = new List[nums.length];
        for(int i = 0; i < nums.length; i++) {
            arr[i] = new ArrayList<Integer>();
        }
        Map<Integer, Integer> map = new HashMap<>();

        for(int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        // create buckets
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            arr[entry.getValue() - 1].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;

        for(int i = arr.length - 1; i >= 0 && index < k; i--) {
            List<Integer> currList = arr[i];
            for (int curr : arr[i]) {
                res[index++] = curr;
            }
        }

        return res;
    }
}