class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = sys.maxsize


        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] >= nums[l]:
                if nums[m] >= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                r = m - 1
            res = min(res, nums[m])
        return res
        