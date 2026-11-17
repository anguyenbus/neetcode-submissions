class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        max_vol = 0
        while left < right:
            width = right - left
            height = min (heights[left], heights[right])
            vol = width * height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            max_vol = max(max_vol, vol)
        return max_vol
