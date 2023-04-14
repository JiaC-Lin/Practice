# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List
from collections import defaultdict

class Solution(object):
# Put numbers into hashmap for each row, column, and 3x3 group and check for repeats
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # avoid keyerror: 0 with defaultdict(list)
        row = defaultdict(list)
        column = defaultdict(list)
        # uses top left most of 3x3 for index by diving and flooring the row and column value by 3
        grid = defaultdict(list) 
        for r in range(9):
            for c in range(9):
                # don't worry about empty - move onto next element
                if board[r][c] == ".":
                    continue 
                # check if number occurred already in row, column, or grid
                if (board[r][c] in row[r] or 
                    board[r][c] in column[c] or 
                    board[r][c] in grid[r // 3, c // 3]):
                    # print("False")
                    return False
                # add number to row, column, and grid for future checks
                else:
                    row[r].append(board[r][c])
                    column[c].append(board[r][c])
                    grid[r // 3, c // 3].append(board[r][c])
        # print("True")
        return True # finished whole board with no falsity

test = Solution()

board1 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

board2 = [["5","8",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

test.isValidSudoku(board1)
test.isValidSudoku(board2)