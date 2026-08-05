class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                old_index = stack.pop()
                res[old_index] = i - old_index
            stack.append(i)
        return res



