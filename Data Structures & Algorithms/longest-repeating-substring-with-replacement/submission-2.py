class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        max_freq=0
        output =0
        l=0
        for r in range (len(s)):
            counts[s[r]]=1+counts.get(s[r],0)
            max_freq=max(max_freq,counts[s[r]])
            if r-l+1-max_freq>k :
                counts[s[l]]-=1
                l+=1
            output=max(output,r-l+1)
        return output



