class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        s_dict, t_dict = {}, {}
        matches = 0
        minLength = sys.maxsize
        res = ""

        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        while r < len(s):
            c = s[r]

            if c in t_dict:
                s_dict[c] = s_dict.get(c, 0) + 1

                # <-- CHANGED: only count a match once
                if s_dict[c] == t_dict[c]:
                    matches += 1

            # <-- CHANGED: shrink as much as possible
            while matches == len(t_dict):

                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    res = s[l:r + 1]

                # <-- CHANGED: remove left character from window
                if s[l] in t_dict:
                    s_dict[s[l]] -= 1

                    # <-- CHANGED: lost a required character
                    if s_dict[s[l]] < t_dict[s[l]]:
                        matches -= 1

                # <-- CHANGED: always move left one step
                l += 1

            r += 1

        return res