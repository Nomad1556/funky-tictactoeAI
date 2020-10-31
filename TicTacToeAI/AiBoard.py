from math import inf
from copy import copy, deepcopy
class AI(object):
    """AI for the player to play against"""
    def __init__(self):
        return super().__init__()

    def minimax(self, board:list, isMaximizer: bool):
        score = self.evaluate_board(board)

        if(self.moves_left(board) == False):
            return score

        if(isMaximizer):
            bestVal = -inf
            boardcopy = deepcopy(board)
            for row in range(0,3):
                for col in range(0,3):
                    if (boardcopy[row][col] == 0):
                        boardcopy[row][col] = 1
                        value = self.minimax(boardcopy,False)
                        bestVal = max(bestVal,value)
        else:
            bestVal = inf
            boardcopy = deepcopy(board)
            for row in range(0,3):
                for col in range(0,3):
                    if (boardcopy[row][col] == 0):
                        boardcopy[row][col] = 2
                        value = self.minimax(boardcopy, True)
                        bestVal = max(bestVal, value)
        return bestVal

    def find_best_move(self, board:list):
        boardcopy = deepcopy(board)
        x,y = -100,-100
        bestMove = -10000
        for row in range(0,3):
            for col in range(0,3):
                if(boardcopy[row][col] == 0): 
                    boardcopy[row][col] = 2
                    currentMove = self.minimax(board, True)
                    if(currentMove > bestMove):
                        bestMove = x
                        x,y = row,col
        return x,y               


    #Check if there are moves left
    def moves_left(self,board:list):
        for row in range(0,3):
            for col in range(0,3):
                if board[row][col] == 0:
                    return True
        return False

    #Heursitic evaluation of the board
    def evaluate_board(self,board:list):
       for row in range(0,3):
         if(board[row][0] == board[row][1] == board[row][2]):
            if(board[row][0] == 1):
                return 10
            elif(board[row][0] == 2):
                return -10
       for col in range(0,3):
        if(board[0][col] == board[1][col] == board[2][col]):
            if(board[0][col] == 1):
                return 10
            elif(board[0][col] == 2):
                return -10
       if(board[0][0] ==  board[1][1] == board[2][2]):
            if(board[0][0] == 1):
                return 10
            elif(board[0][0] == 2):
                return -10
       elif(board[2][0] == board[1][1] == board[0][2]):
            if(board[2][0] == 1):
                return 10
            elif(board[2][0] == 2):
                return -10
       return 0


if __name__ == "__main__":
    blank = '-'
    Xspace = 'x'
    Ospace = 'o'

    board = [[blank] *3 , [blank] * 3, [blank] * 3]
    testAI = AI()

    board[1][2] = Xspace
    board[1][1] = Xspace
    board[2][1] = Ospace
    board[0][1] = Ospace
    board[0][2] = Ospace

    x,y = testAI.find_best_move(board)
    print("Best move is row: {} and {}".format(x,y))
