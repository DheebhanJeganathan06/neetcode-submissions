class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        longest = 1

        while r < len(s):
            set = {s[l]}
            while r < len(s) and s[r] not in set:
                set.add(s[r])
                r += 1
            longest = max(longest, len(set))
            l, r = l + 1, l + 2
        return longest

        