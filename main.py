#___________________________________________________________________________________________________________


def sum(a, b, c):
    return a + b + c


def gameBoard(xValue,yValue):
    zero = 'X' if xValue[0] else ('O' if yValue[0] else 0)
    one = 'X' if xValue[1] else ('O' if yValue[1] else 1)
    two = 'X' if xValue[2] else ('O' if yValue[2] else 2)
    three = 'X' if xValue[3] else ('O' if yValue[3] else 3)
    four = 'X' if xValue[4] else ('O' if yValue[4] else 4)
    five = 'X' if xValue[5] else ('O' if yValue[5] else 5)
    six = 'X' if xValue[6] else ('O' if yValue[6] else 6)
    seven = 'X' if xValue[7] else ('O' if yValue[7] else 7)
    eight = 'X' if xValue[8] else ('O' if yValue[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def checkWin(xValue,yValue):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xValue[win[0]], xValue[win[1]], xValue[win[2]]) == 3):
            print("X Won the match")
            return 1
        if (sum(yValue[win[0]], yValue[win[1]], yValue[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1


if __name__ == "__main__":
    xValue = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yValue = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while (True):
        gameBoard(xValue, yValue)
        if (turn == 1):
            print("X's Chance")
            value = int(input("Please enter value in: "))
            xValue[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter value in: "))
            yValue[value] = 1
        cwin = checkWin(xValue, yValue)
        if (cwin != -1):
            print("Match over")
            break

        turn = 1 - turn

