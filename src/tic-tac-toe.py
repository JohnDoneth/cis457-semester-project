import random
import time

class Game:

    def Game():
        for i in range(random.randint(1, 500)):
            player = random.randint(1, 2)
        TicTacToe = Game(player)

    def __init__(self, player):
        print('Here is a reference to what spots are what\n')
        self.refBoard = '1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n'
        print(self.refBoard)
        self.play = 0
        self.boardStr = '\n | | \n-+-+-\n | | \n-+-+-\n | | \n'
        print(self.boardStr)
        if player == 1:
            Game.Start(self,'player', board=self.boardStr)
        elif player == 2:
            Game.Start(self,'CPU', board=self.boardStr)
        
    def Start(self, starter, board):
        if starter == 'player':
            player = 'X'
            CPU = 'O'
            start = 1
            print("You are X's")
        elif starter == 'CPU':
            player = 'O'
            CPU = 'X'
            start = 0
            print("You are O's")
            print("\nComputer goes first")
        Game.Play(self, player, CPU, start, board)

    def Play(self, player, CPU, start, board):
        if start == 0:
            start = 1
            spot = random.randint(0, 8)
            sym = CPU
            Game.Move(self, sym, spot, player, CPU, board)
            Game.Play(self, player, CPU, start, board)
        else:
            start = 0
            spot = input('\nChoose the spot you want to put your %s (1-9): ' % player)
            if spot == '1':
                pass
            elif spot == '2':
                pass
            elif spot == '3':
                pass
            elif spot == '4':
                pass
            elif spot == '5':
                pass
            elif spot == '6':
                pass
            elif spot == '7':
                pass
            elif spot == '8':
                pass
            elif spot == '9':
                pass
            else:
                print('\nInvalid Choice\n')
                Game.Play(self, player, CPU, 1, board)
            spot = int(spot)-1
            sym = player
            Game.Move(self, sym, spot, player, CPU, board)
            Game.Play(self, player, CPU, start, board)

    def Move(self, sym, spot, player, CPU, board):
        
        board = list(board)
        
        for i in range(6):
            board.remove('|')
            board.remove('-')
            board.remove('\n')
        for i in range(4):
            board.remove('+')

        if ' ' in board:
            pass
        else:
            print("Tied Game\n")
            time.sleep(2)
            Game.Game()
        
        if board[spot] == ' ':
            board[spot] = sym
        else:
            board.insert(1, '|')
            board.insert(3, '|')
            board.insert(5, '\n')
            board.insert(6, '-')
            board.insert(7, '+')
            board.insert(8, '-')
            board.insert(9, '+')
            board.insert(10, '-')
            board.insert(11, '\n')
            board.insert(13, '|')
            board.insert(15, '|')
            board.insert(17, '\n')
            board.insert(18, '-')
            board.insert(19, '+')
            board.insert(20, '-')
            board.insert(21, '+')
            board.insert(22, '-')
            board.insert(23, '\n')
            board.insert(25, '|')
            board.insert(27, '|')
            board.insert(29, '\n')
            board.insert(0, '\n')
            board = "".join(board)
            if sym == player:
                print('\nSpot already Taken try again\n')
                Game.Play(self, player, CPU, 1, board)
            else:
                Game.Play(self, player, CPU, 0, board)
  
        board.insert(1, '|')
        board.insert(3, '|')
        board.insert(5, '\n')
        board.insert(6, '-')
        board.insert(7, '+')
        board.insert(8, '-')
        board.insert(9, '+')
        board.insert(10, '-')
        board.insert(11, '\n')
        board.insert(13, '|')
        board.insert(15, '|')
        board.insert(17, '\n')
        board.insert(18, '-')
        board.insert(19, '+')
        board.insert(20, '-')
        board.insert(21, '+')
        board.insert(22, '-')
        board.insert(23, '\n')
        board.insert(25, '|')
        board.insert(27, '|')
        board.insert(29, '\n')
        board.insert(0, '\n')
        board = "".join(board)

        print('%s' % board)
        
        Check = Game.CheckWin(self, sym, board)
        if Check == False:
            pass
        elif Check == True:
            if sym == player:
                print('Congrats You Won\n')
                time.sleep(2)
                Game.Game()
            else:
                print('Sorry You Lost\n')
                time.sleep(2)
                Game.Game()
        
        if sym == player:
            print('\nComputers Turn:\n')
            Game.Play(self, player, CPU, 0, board)
        else:
            Game.Play(self, player, CPU, 1, board)


    def CheckWin(self, sym, board):
        board = list(board)
        for i in range(6):
            board.remove('|')
            board.remove('-')
            board.remove('\n')
        for i in range(4):
            board.remove('+')
        
        if sym == 'X':
            if board[0] == board[1] == board[2] == 'X':
                return True
            elif board[3] == board[4] == board[5] == 'X':
                return True
            elif board[6] == board[7] == board[8] == 'X':
                return True
            elif board[0] == board[3] == board[6] == 'X':
                return True
            elif board[1] == board[4] == board[7] == 'X':
                return True
            elif board[2] == board[5] == board[8] == 'X':
                return True
            elif board[0] == board[4] == board[8] == 'X':
                return True
            elif board[2] == board[4] == board[6] == 'X':
                return True
            else:
                return False
        elif sym == 'O':
            if board[0] == board[1] == board[2] == 'O':
                return True
            elif board[3] == board[4] == board[5] == 'O':
                return True
            elif board[6] == board[7] == board[8] == 'O':
                return True
            elif board[0] == board[3] == board[6] == 'O':
                return True
            elif board[1] == board[4] == board[7] == 'O':
                return True
            elif board[2] == board[5] == board[8] == 'O':
                return True
            elif board[0] == board[4] == board[8] == 'O':
                return True
            elif board[2] == board[4] == board[6] == 'O':
                return True
            else:
                return False

if __name__ == "__main__":
    Game.Game()
