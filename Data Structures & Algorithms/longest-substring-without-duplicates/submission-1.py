class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=[]
        output=0
        for i in range (len(s)):
            if i==0 :
                L.append(s[i])
                output=1
            else : 
                if s[i] not in L :
                    L.append(s[i])
                    output=max(output,len(L))
                else: 
                    n=L.index(s[i])
                    del L[0:n+1]
                    L.append(s[i])
                    output=max(output,len(L))
        return output 



