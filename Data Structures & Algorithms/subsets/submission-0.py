class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            new_subsets = []
            for arr in res:
                dup_arr = arr.copy()
                dup_arr.append(num)
                new_subsets.append(dup_arr)

            res.extend(new_subsets)

        return res
        