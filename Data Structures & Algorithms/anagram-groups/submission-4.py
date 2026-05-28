class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_dict = {}
        for s in strs:
            count_list = [0] * 26
            for c in s:
                count_list[ord(c) - ord('a')] += 1
            list_dict.setdefault(str(count_list), []).append(s)
        return list(list_dict.values())
            