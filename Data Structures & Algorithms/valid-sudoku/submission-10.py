import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_small(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    vis=[]
                    for p in range(i,i+3):
                        for q in range(j, j+3):
                            if board[p][q]==".":
                                pass
                            else:
                                if board[p][q] in vis:
                                    return False
                                else:
                                    vis.append(board[p][q])
            return True
        def check_big(board):
            for i in range(9):
                vis=[]
                for j in range(9):
                    if board[i][j]==".":
                        pass;
                    else:
                        if board[i][j] in vis:
                            return False
                        else:
                            vis.append(board[i][j])
        a1=check_big(board)
        b=np.transpose(board).tolist()
        a2=check_big(b)
        a3=check_small(board)
        if a1==False:
            return False
        if a2==False:
            return False
        if a3==False:
            return False
        return True