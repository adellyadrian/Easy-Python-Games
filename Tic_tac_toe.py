player_1 = input("")
player_2 = input("")
board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(row)


def victory():
    if board[0] == board[1] == board[2] != " ":
        return True
    if board[3] == board[4] == board[5] != " ":
        return True
    if board[6] == board[7] == board[8] != " ":
        return True
    if board[0] == board[3] == board[6] != " ":
        return True
    if board[1] == board[4] == board[7] != " ":
        return True
    if board[2] == board[5] == board[8] != " ":
        return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False


while True:
    print_board()
    while True:
        try:
            step = int(input(f"{player_1}"))
            if step < 0 or step > 8 or board[step] != " ":
                raise ValueError
            break
        except ValueError:
            print("Try again.")

    board[step] = "X"

    if victory():
        print_board()
        print(f"{player_1} wins")
        break

    if " " not in board:
        print_board()
        print("No one")
        break

    print_board()
    while True:
        try:
            step = int(input(f"{player_2}"))
            if step < 0 or step > 8 or board[step] != " ":
                raise ValueError
        except ValueError:
            print("Try again")
            break
        board[step] = "O"

    if victory():
        print_board()
        print(f"{player_2} wins!")
        break
