class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            emb = [0 for _ in range(26)]

            for c in s:
                emb[ord(c)-ord('a')]+=1
                
            d[tuple(emb)].append(s)

        return list(d.values())
