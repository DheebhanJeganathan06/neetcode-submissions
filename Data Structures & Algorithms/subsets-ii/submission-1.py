class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            # if we've found a valid subset (noted by length), we add it to res
            # we also don't do anything more on this branch as it is completed
            if i == len(nums):
                res.append(subset.copy())
                return

            # case 1: we add the current value (and are open to adding all dupes of that value)
            # we append the i'th value to our subset
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # case 2: we do not add the current value (and skip over duplicates)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        # initial call starts at index 0 and empty set
        backtrack(0, [])
        # safely return res after backtrack is done iterating
        return res