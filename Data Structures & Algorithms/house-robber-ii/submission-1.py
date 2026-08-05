class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.helper(nums, 1, len(nums)),
            self.helper(nums, 0, len(nums) - 1)
        )

    def helper(self, nums, left, right):
        rob1, rob2 = 0, 0

        for i in range(left, right):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2