class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        shortest = sys.maxsize
        res = ""

        letterMapping = {}
        t_letterList = []
        i = 0
        for c in t:
            if c not in letterMapping:
                letterMapping[c] = i
                i += 1
                t_letterList.append(1)
            else:
                t_letterList[letterMapping[c]] += 1

        s_letterList = [0] * len(t_letterList)
        matches = 0

        # REMOVED:
        # queue = deque()

        l = 0
        while l < len(s) and s[l] not in letterMapping:
            l += 1

        for r in range(l, len(s)):
            if s[r] in letterMapping:
                s_letterList[letterMapping[s[r]]] += 1

                # REMOVED:
                # queue.append(r)

                if s_letterList[letterMapping[s[r]]] == t_letterList[letterMapping[s[r]]]:
                    matches += 1

            while matches == len(t_letterList):
                if (r - l + 1) < shortest:
                    res = s[l:r + 1]
                    shortest = len(res)

                s_letterList[letterMapping[s[l]]] -= 1
                if s_letterList[letterMapping[s[l]]] < t_letterList[letterMapping[s[l]]]:
                    matches -= 1

                # CHANGED: advance l directly
                l += 1
                while l < len(s) and s[l] not in letterMapping:
                    l += 1

        return res