class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validateRow(self, row: int) -> bool:
            s = set()
            for i in board[row]:
                if i != '.' and i in s:
                    return False
                s.add(i)
            return True
        
        def validateCol(self, j: int) -> bool:
            s = set()
            for i in range(9):
                c = board[i][j]
                if c != '.' and c in s:
                    return False
                s.add(c)
            return True

        def validateSector(self, x: int, y: int) -> bool:
            s = set()
            for i in range(x, x + 3):
                for j in range(y, y+3):
                    l = board[i][j]
                    if l != '.' and l in s:
                        return False
                    s.add(l)
            return True

        for j in range(9):
            if not validateRow(self, j):
                return False
            if not validateCol(self, j):
                return False

        # validateSector(self, 0,0)

        for i in range(3):
            for j in range(3):
                if not validateSector(self, i * 3, j * 3):
                    return False
        

        return True

