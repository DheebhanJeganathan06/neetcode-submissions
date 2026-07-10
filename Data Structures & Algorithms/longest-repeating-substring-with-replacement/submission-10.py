class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        letter_counts = {}
        max_freq = 0
        res = 0

        while r < len(s):
            # add current letter to map
            letter_counts[s[r]] = letter_counts.get(s[r], 0) + 1
            max_freq = max(max_freq, letter_counts[s[r]])

            # increment l until valid substring is reached
            while l < len(s) and ((r - l + 1) - max_freq > k):
                letter_counts[s[l]] = letter_counts.get(s[l], 0) - 1
                l += 1
            res = max(res, r - l)
            r += 1

        return max(res, r - l)
        