
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkCol(cols):
            l = 9
            for j in range(l):
                s = set()
                for i in range(l):
                    if cols[i][j] == '.': continue
                    if cols[i][j] in s:
                        return False
                    else: s.add(cols[i][j])
            return True
        def checkRows(rows):
            l = 9
            for i in range(l):
                s = set()
                for j in range(l):
                    if rows[i][j] == '.': continue
                    if rows[i][j] in s:
                        return False
                    else: s.add(rows[i][j])
            return True
        def checkBox(board):
            for k in range(3):
                for n in range(3):
                    s = set()
                    for i in range(k*3,3 + 3*k):
                        for j in range(3*n,3+n*3):
                            pass
                            if board[i][j] == '.': continue
                            if board[i][j] in s:
                                return False
                            else: s.add(board[i][j])
            return True
                    
        return checkCol(board) and checkRows(board) and checkBox(board)
# a better solution        
#class Solution:
#    def isValidSudoku(self, board: List[List[str]]) -> bool:
#        rows = [[False] * 9 for _ in range(9)]
#        cols = [[False] * 9 for _ in range(9)]
#        boxes = [[False] * 9 for _ in range(9)]
#
#        for i in range(9):
#            for j in range(9):
#                if board[i][j] != '.':
#                    num = ord(board[i][j]) - ord('1')
#                    boxIndex = (i // 3) * 3 + (j // 3)
#                    if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
#                        return False
#                    rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True
#        return True
