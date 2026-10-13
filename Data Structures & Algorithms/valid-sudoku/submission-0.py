class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for i in range (9):
            for j in range (9):
                val=board[i][j]
                if val!=".":
                    raw_seen= f"{val} dans ligne {i}"
                    col_seen= f"{val} dans colonne {j}"
                    box_seen= f"{val} dans carré ({i//3},{j//3})"
                    if raw_seen in seen or col_seen in seen or box_seen in seen:
                        return False
                    seen.add(raw_seen)
                    seen.add(col_seen)
                    seen.add(box_seen)
        return True
