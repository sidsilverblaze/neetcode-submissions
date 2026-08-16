#from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        vals = [[] for i in range(len(nums)+1)]
        
        for num,cnt in count.items():
            vals[cnt].append(num)
        
        res = []
        for i in range(len(vals)-1,0,-1):
            for v in vals[i]:
                res.append(v)
                if len(res)==k:
                    return res
        