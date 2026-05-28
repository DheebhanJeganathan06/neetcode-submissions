class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        iter = nums[0]
        for i in range(1, len(nums)):
            res[i] *= iter
            iter *= nums[i]
        
        iter = nums[len(nums) - 1]
        for i in reversed(range(0, len(nums) - 1)):
            res[i] *= iter
            iter *= nums[i]
        return res
            