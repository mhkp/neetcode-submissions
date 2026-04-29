class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        sorted_keys = sorted(c.keys(), key=c.get,reverse=True)
        return sorted_keys[:k]
        