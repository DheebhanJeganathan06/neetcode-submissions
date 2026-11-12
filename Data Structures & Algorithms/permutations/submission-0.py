class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case: empty list simply returns list with empty array as only entry
        if len(nums) == 0:
            return [[]]

        # work "recursively" to create all (n-1) sized permutations excluding
        # the current index's value
        perms = self.permute(nums[1:])
        # result array after adding current value at
        # all possible indices of perms arrays
        res = []
        # iterate over all (n-1) sets in perms
        for p in perms:
            # iterate over all possible indices to insert value
            # we extend by 1 because you could add it at the end
            for i in range(len(p) + 1):
                # create copies bc list references carry memory position
                p_copy = p.copy()
                # insert current value at the currently chosen index
                p_copy.insert(i, nums[0])
                # add the new perm to res
                res.append(p_copy)
        # each call returns res, which gets set to perms for parent call
        # initial call can safely return res as the final answer
        return res
        