class Solution:
    def isValid(self, s: str) -> bool:
        elements=[")","(","{","}","[","]"]
        L=[]      
        for i in range (len(s)):
            if s[i] in elements :
                if s[i] in [")","}","]"] and L==[]:
                    return False
                if (s[i]==")" and L[-1]!="(") or (s[i]=="}" and L[-1]!="{") or (s[i]=="]" and L[-1]!="[") :
                    return False
                if (s[i]==")" and L[-1]=="(") or (s[i]=="}" and L[-1]=="{") or (s[i]=="]" and L[-1]=="[") :
                    del L[-1]
                if s[i] in ["(","{","["] :
                    L.append(s[i])

        return L==[]
        