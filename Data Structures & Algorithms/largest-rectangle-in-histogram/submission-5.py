class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = deque()

        for i, height in enumerate(heights):
            curr_index = i
            while stack and stack[-1][1] > height:
                old_val = stack.pop()
                old_index, old_height = old_val[0], old_val[1]
                maxArea = max(maxArea, old_height * (i - old_index))
                curr_index = old_index
            stack.append([curr_index, height])

        while stack:
            old_val = stack.pop()
            old_index, old_height = old_val[0], old_val[1]
            maxArea = max(maxArea, old_height * (len(heights) - old_index))

        return maxArea
