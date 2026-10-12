class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      dictS={}
      dictT={}

      for x in s :
        dictS[x]=dictS.get(x,0)+1
      for x in t :
        dictT[x]=dictT.get(x,0)+1 
      return dictS==dictT   