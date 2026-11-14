class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        res = []
        map = {"2": ['a', 'b', 'c'],
               "3": ['d', 'e', 'f'],
               "4": ['g', 'h', 'i'],
               "5": ['j', 'k', 'l'],
               "6": ['m', 'n', 'o'],
               "7": ['p', 'q', 'r', 's'],
               "8": ['t', 'u', 'v'],
               "9": ['w', 'x', 'y', 'z']}
        

        def dfs(curr, i):
            if i == len(digits):
                res.append("".join(curr))
                return

            for letter in map.get(digits[i]):
                curr.append(letter)
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return res
        