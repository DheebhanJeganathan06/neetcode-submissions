class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = {}
        res = [0] * len(temperatures)
        for i, a in enumerate(temperatures):
            if stack:
                while stack and (a > list(stack.values())[-1]):
                    key, val = stack.popitem()
                    res[key] = i - int(key)
            stack[i] = a
        return res

