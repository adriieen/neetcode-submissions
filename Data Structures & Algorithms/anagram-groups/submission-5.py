class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = [(i,sorted(strs[i])) for i in range(len(strs))]
        l = sorted(l, key=lambda x:x[1])

  
        if len(l)==1:
            return [strs]

        idx = []
        idx_words = [l[0][0]]
        i=0
        while i<len(l):
            if i<len(l)-1 and l[i][1]==l[i+1][1]:
                idx_words.append(l[i+1][0])

            else:
                idx.append(idx_words)
                if i<=len(l)-2:
                    idx_words=[l[i+1][0]]
            i+=1
        
        output=[]
        for idx_word in idx:
            output.append([strs[i] for i in idx_word])
        return output
            
