class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] arr = new List[nums.length + 1];
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < arr.length; i++) {
            arr[i] = new ArrayList<>();
        }

        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            arr[entry.getValue()].add(entry.getKey());
        }

        int[] res  = new int[k];
        int index = 0;

        for(int i = arr.length - 1; i >= 0 && index < k; i--) {
            for(int j : arr[i]) {
                res[index++] = j;
                if(index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
