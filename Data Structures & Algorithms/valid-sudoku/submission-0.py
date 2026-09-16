#Time comp: O(N^2), where N is size of sudoku board (here 9, so O(9^2) = O(81))
#Space comp: O(1), hash maps (rows, cols, squares) storing at most 9 entries per structure
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initialize HashSet (dictionary of key:val where val is set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # sub-squars(3X3) in 9X9 sudoku -> (key,val): (r/3, c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # checking if cell is empty denoted by "."
                    continue           # because we are only validating for filled cells
                
                if ( board[r][c] in rows[r] or
                     board[r][c] in cols[c] or
                     board[r][c] in squares[(r//3, c//3)] ):
                   return False
                #else add the curent vals to hashsets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True #sudoku is valid otherwise