from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window approach
        expected = Counter(s1)
        left = 0
        actual = defaultdict(int)
        for right in range(len(s2)):
            actual[s2[right]] += 1
            while actual[s2[right]] > expected[s2[right]]:
                actual[s2[left]] -= 1
                left += 1
            if (right - left + 1) == len(s1):
                return True
        return False

        # 