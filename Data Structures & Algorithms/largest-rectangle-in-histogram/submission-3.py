class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index, height in enumerate(heights):
            if not stack or stack[-1][1] < height:
                stack.append((index, height))
            else:
                newIndex = index
                while stack and stack[-1][-1] > height:
                    popped = stack.pop()
                    maxArea = max(popped[1] * (index - popped[0]), maxArea)
                    newIndex = popped[0]
                stack.append((newIndex, height))

        while stack:
            index, height = stack.pop()
            maxArea = max(height * (len(heights) - index), maxArea)

        return maxArea
