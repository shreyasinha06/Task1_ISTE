def game():
    board=list()
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win= [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def draw():
        i=0
        while i<len(board):
           print(board[i]," ",board[i+1]," ",board[i+2])
           i=i+3

    def p1():
        n = choose_number()
        if board[n] == "SH" or board[n] == "AN":
            print("\ncan't go there:((")
            p1()
        else:
            board[n] = "SH"

    def p2():
        n = choose_number()
        if board[n] == "SH" or board[n] == "AN":
            print("\n can't go there:((")
            p2()
        else:
            board[n] = "AN"

    def choose_number():
        while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\n not on the board :( TRY AGAIN")
                        continue
                except ValueError:
                   print("\n not a number:( TRY AGAIN")
                   continue

    def check_board():
        count = 0
        for a in win:
            if board[a[0]] == board[a[1]] == board[a[2]] == "SH":
                print(" Congratulations Shreya!\n")
              
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "AN":
                print("Congratulations Ananya !\n")
                
                return True
        for a in range(9):
            if board[a] == "SH" or board[a] == "AN":
                count += 1
            if count == 9:
                print("game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Shreya choose where to place SH")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Ananya choose where to place a AN")
        p2()
        print()

    if input("Play again (yes/no)\n") == "yes":
        print()
        game()

game()
