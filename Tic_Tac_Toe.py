def print_board(Board):
    print(f"\n{Board[0]} | {Board[1]} | {Board[2]} ")
    print("--+---+--")
    print(f"{Board[3]} | {Board[4]} | {Board[5]} ")
    print("--+---+--")
    print(f"{Board[6]} | {Board[7]} | {Board[8]} \n")

board = [" "]*9

def check_win(player):
    return (
        (board[0] == board[1] == board[2] == player)or  #row
        (board[3] == board[4] == board[5] == player)or
        (board[6] == board[7] == board[8] == player)or
        (board[0] == board[3] == board[6] == player)or  #column
        (board[1] == board[4] == board[7] == player)or
        (board[2] == board[5] == board[8] == player)or
        (board[0] == board[4] == board[8] == player)or
        (board[2] == board[4] == board[6] == player)
    )

def isEmpty(Board):
    for i in range(0, 9):
        if(Board[i] == " "):
            return True
    return False

def play():
    player = "X"
    winner = False
    print_board(board)

    while(isEmpty(board)):
        print(f"Now turn {player}")
        Entry = int(input("Enter the move on Board (Enter From 1 to 9) : "))
        if(board[Entry-1] == " "):
            board[Entry-1] = player
        else:
            print("The Space Is Already taken Please Enter valid Number")
            continue 

        print_board(board)
        if(check_win(player)):
            print(f"Congratulations Player {player} Won !!!")
            winner = True
            break

        if(player == "X"):
            player = "O"
        else:
            player = "X"
        
    if(not winner):
        print("OOPS!! IT's a Draw Match")

play()

    


        
        
