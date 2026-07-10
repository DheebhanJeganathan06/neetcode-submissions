class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        letterSet = set()

        while r < len(s):
            if s[r] not in letterSet:
                letterSet.add(s[r])
            else:
                repeatChar = s[r]
                res = max(res, r - l)
                while s[l] != s[r]:
                    letterSet.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return max(res, r - l)
        