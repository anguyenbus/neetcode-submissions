class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for v, f in count.items():
            buckets[f].append(v)

        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for v in buckets[f]:
                res.append(v)
                if len(res) == k:
                    return res
        return res