#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

class TicTacToe:

    def grid(w, h):
        for i in range(h):
            print(' --- ' * w)
            print('|  ' * w + w*i + '|')
        print(' --- ' * w)


    def startGame():
        moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print('Hello to TicTacToe!')
        print('Your move! Possible moves are: ' + str(moves))
        grid(3, 3)
        move = int(input('Move: '))


if __name__ == '__main__':
    startGame()
