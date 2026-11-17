class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window approach
        k = len(s1)
        if k > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        for i in range(k):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        if window == need:
            return True
        for right in range(k, len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[right - k]) -ord('a')] -= 1
            if window == need:
                return True
        return False
        # 