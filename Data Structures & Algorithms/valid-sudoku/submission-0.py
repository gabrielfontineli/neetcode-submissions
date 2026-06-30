class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lines = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        blocks =[set() for i in range(9)]
        
        for l in range(9):
            for c in range(9):
                block_index = (l//3)*3+(c//3)

                current = board[l][c]
                if board[l][c] == ".":
                    continue
                if current in lines[l] or current in cols[c] or current in blocks[block_index]:
                    return False
                
                lines[l].add(current)
                cols[c].add(current)
                blocks[block_index].add(current)

        return True
                
        
