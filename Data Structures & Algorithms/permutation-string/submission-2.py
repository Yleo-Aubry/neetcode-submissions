class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1={}
        dict2={}
        for i in range(len(s1)):
            dict1[s1[i]]=1+dict1.get(s1[i],0)
        
        for i in range (len(s2)-len(s1)+1):
            for j in range(i,i+len(s1)):
                dict2[s2[j]]=1+dict2.get(s2[j],0)
            if dict2==dict1 :
                return True
            else :
                dict2={}
        return False