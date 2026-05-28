class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = set()
        for num in nums:
            if num in num_list:
                return True
            num_list.add(num)
        return False