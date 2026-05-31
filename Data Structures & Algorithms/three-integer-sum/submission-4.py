class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = 0
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l - 1] == nums[l]:
                        l += 1
                    r -= 1
                    while r > 0 and nums[r + 1] == nums[r]:
                        r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res
        