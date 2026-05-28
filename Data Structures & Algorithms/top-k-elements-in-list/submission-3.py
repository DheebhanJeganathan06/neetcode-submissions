class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        
        count_dict = {0:[]}
        for num in num_dict:
            freq = num_dict[num]
            if freq not in count_dict:
                count_dict[freq] = []
            count_dict.setdefault(freq, []).append(num)
        
        res = []
        for freq in range(len(nums), 0, -1):
            if freq in count_dict:
                for num in count_dict[freq]:
                    res.append(num)

                    if len(res) == k:
                        return res