class Solution:
    def isunique(self,arr):
        nums = [i for i in arr if i != "."]

        print(set(nums),len(nums) == len(set(nums)))
        return len(nums) == len(set(nums))




    def isValidSudoku(self, board):
        for b in board:
            if not self.isunique(b):
                return False
        # check 3x3 boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                box = [board[r][c] for r in range(br, br+3) for c in range(bc, bc+3)]
                if not self.isunique(box):
                    return False
        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not self.isunique(col):
                return False
        
        return True
        