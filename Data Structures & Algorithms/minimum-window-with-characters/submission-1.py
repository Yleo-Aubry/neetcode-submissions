class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tab1 = {}
        tab2 = {}
        for i in range(len(t)):
            tab1[t[i]] = tab1.get(t[i], 0) + 1
        l = 0
        min_len = float('inf')
        res = ""
        for r in range(len(s)):
            x = s[r]
            tab2[x] = tab2.get(x, 0) + 1
            while l <= r and tab2[s[l]] > tab1.get(s[l], 0):
                y = s[l]
                tab2[y] = tab2.get(y, 0) - 1
                l += 1
            match=True
            
            for x_j, count in tab1.items():
                if tab2.get(x_j, 0) < count:
                    match=False
                    break
                
            if match and (r - l + 1) < min_len:
                min_len = r - l + 1
                res = s[l:r+1]
        return res
