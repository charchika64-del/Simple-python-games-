board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def layout_structure():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def change(number, symbol):
    index = number - 1
    board[index] = symbol

def win():
    horizontal1 = [board[0], board[1], board[2]]
    horizontal2 = [board[3], board[4], board[5]]
    horizontal3 = [board[6], board[7], board[8]]
    vertical1   = [board[0], board[3], board[6]]
    vertical2   = [board[1], board[4], board[7]]
    vertical3   = [board[2], board[5], board[8]]
    diagonal1   = [board[0], board[4], board[8]]
    diagonal2   = [board[2], board[4], board[6]]
    
    arrangements = [horizontal1, horizontal2, horizontal3, vertical1, vertical2, vertical3, diagonal1, diagonal2]
    
    for arrangement in arrangements:
        unique = set(arrangement)
        if len(unique) == 1:
            if arrangement[0] == "O":
                print("O wins!")
                return True     
            else:
                print("X wins!")
                return True
    return False

layout_structure()
Win = False
turns = 0

while not Win:
    # --- Player O Turn ---
    while True:
        user1 = int(input("O's turn! Which number to replace? "))
        if 1 <= user1 <= 9 and board[user1 - 1] not in ["X", "O"]:
            break
        print("Invalid choice or spot already taken! Try again.")

    change(user1, "O")
    turns += 1
    layout_structure()
    
    Win = win()
    if Win:
        break
    if turns == 9:
        print("It's a tie!")
        break

    # --- Player X Turn ---
    while True:
        user2 = int(input("X's turn! Which number to replace? "))
        if 1 <= user2 <= 9 and board[user2 - 1] not in ["X", "O"]:
            break
        print("Invalid choice or spot already taken! Try again.")

    change(user2, "X")
    turns += 1
    layout_structure()
    
    Win = win()
    if Win:
        break
    if turns == 9:
        print("It's a tie!")
        break
  
