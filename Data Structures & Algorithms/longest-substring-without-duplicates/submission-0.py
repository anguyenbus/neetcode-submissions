class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        maxLength = 0
        window = set()
        while right < n:
            # main algo, check duplicates
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            maxLength = max(maxLength, right - left + 1)
            # keep moving right
            right += 1
        return maxLength