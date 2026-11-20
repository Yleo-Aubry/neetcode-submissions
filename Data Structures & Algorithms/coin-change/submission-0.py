class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def dfs(i, reste):
            if reste == 0:
                return 0
            if reste < 0 or i < 0:
                return float('inf')
            if (i, reste) in mem:
                return mem[(i, reste)]
            utiliser = 1 + dfs(i, reste - coins[i])
            passer = dfs(i - 1, reste)
            mem[(i, reste)] = min(utiliser, passer)
            return mem[(i, reste)]
        resultat = dfs(len(coins) - 1, amount)
        return resultat if resultat != float('inf') else -1
            
