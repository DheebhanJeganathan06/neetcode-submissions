class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        els = set()

        for num in nums:
            els.add(num)
        
        sts = set()

        for num in els:
            if (num - 1) not in els:
                sts.add(num)

        longest = 0

        for st in sts:
            curr = st
            length = 1
            while (curr + 1) in els:
                curr += 1
                length += 1
            if length > longest:
                longest = length
    
        return longest
        