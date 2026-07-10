class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        l, r = 0, 0
        matches = 0
        s1_dict, s2_dict = {}, {}

        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1

        while r < len(s2):
            if matches == len(s1_dict): return True
            
            c_r = s2[r]
            if c_r in s1_dict:
                s2_dict[c_r] = s2_dict.get(c_r, 0) + 1
                if s2_dict[c_r] == s1_dict[c_r]:
                    matches += 1
                while s2_dict[c_r] > s1_dict[c_r]:
                    c_l = s2[l]
                    if (c_l in s1_dict) and (s2_dict[c_l] == s1_dict[c_l]):
                        matches -= 1
                    s2_dict[c_l] = s2_dict.get(c_l, 0) - 1
                    l += 1
            else:
                l = r + 1
                matches = 0
                s2_dict = {}
            r += 1

        return matches == len(s1_dict)
        