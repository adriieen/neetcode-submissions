class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] +=1
        
        l = [(n,d[n]) for n in list(d.keys())]
        l = sorted(l, key = lambda x:x[1])
        
        return([couple[0] for couple in l[-k:]])
