class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        
        for word in strs :
            s+=str(len(word))
            s+="#"
            s+= word 
        return s 
    def decode(self, s: str) -> List[str]:
        i=0
        strs=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
                
            length=int(s[i:j])
            strs.append(s[j+1:j+length+1])
            i=j+length+1
        
        
        return strs




