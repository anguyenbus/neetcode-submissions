from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window approach
        expected = Counter(s1)
        left = 0
        actual = defaultdict(int)
        for right in range(len(s2)):
            char = s2[right]
            actual[char] += 1
            # moving window
            while actual[char] > expected[char]:
                # shift left
                leftmost_char = s2[left]
                actual[leftmost_char] -= 1
                left += 1
            if (right - left + 1) == len(s1):
                return True
        return False