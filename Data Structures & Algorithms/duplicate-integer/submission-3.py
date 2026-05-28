class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = []
        for num in nums:
            if num in num_list:
                return True
            num_list.append(num)
        return False