class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        r,l=len(s)-1,0
        while r>l :
            if s[l]!=s[r]:
                return False
            else: 
                r-=1
                l+=1
        return True