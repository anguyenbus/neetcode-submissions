class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx              # extend the new bar backwards
            stack.append((start, h))

        n = len(heights)
        for idx, height in stack:        # these reached the right edge
            max_area = max(max_area, height * (n - idx))

        return max_area