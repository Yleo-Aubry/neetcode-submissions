class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tab1=[0]*26
        tab2=[0]*26
        l=0
        for i in range(len(s1)):
            tab1[ord(s1[i])-ord('a')]+=1
        for i in range(len(s2)):
            tab2[ord(s2[i])-ord('a')]+=1
            if i-l+1>len(s1):
                tab2[ord(s2[l])-ord('a')]-=1
                l+=1
            if tab1==tab2:
                return True
        return False