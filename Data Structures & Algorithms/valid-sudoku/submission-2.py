class Solution:
    def check_square(self, board: List[List[str]], x, y, a, b) -> bool:

        s = set()
        for i in range(x, y):
            for j in range(a, b):
                if board[i][j] != "." and board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            s = set()
            s2 = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

                if board[j][i] != "." and board[j][i] in s2:
                    return False
                else:
                    s2.add(board[j][i])
        n, m, a, b = 0, 3, 0, 3
        for i in range(1, 10):
            if self.check_square(board, n, m, a, b) == False:
                return False
            n, m = m, m + 3
           
            if i % 3 == 0:
                a, b = b, b + 3
                n, m = 0, 3

        return True
            


