#from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        sorted_counts = sorted(count, reverse=True, key = lambda x: count[x])
        return sorted_counts[:k]
        