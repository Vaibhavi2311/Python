import random
board=["" for _ in range(9)]

def display_board():
    print()
    print(board[0] + " | " +board[1] + " | " +board[2])
    print("--+---+--")
    print(board[3] + " | " +board[4] + " | " +board[5])
    print("--+---+--")
    print(board[6] + " | " +board[7] + " | " +board[8])
    print("--+---+--")
    
def check_winner(player):
    wining_positions=[
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]
    
    for a,b,c in wining_positions:
        if board[a]==board[b]==board[c]==player:
            return True
    return False

def check_draw():
    return "" not in board

def computer_move():
    empty_positions=[]
    
    for i in range(9):
        if board[i]=="":
            empty_positions.append(i)
            
    position=random.choice(empty_positions)
    board[position]="0"

def play_game():
    print("🎮 TIC-TAC-TOE")
    print("You are X")
    print("Computer is O")

   
    
    while True:
        display_board()
        
        try:
            position=int(input("Enter a position(1-9):"))-1
            
        except ValueError:
            print("Please enter a number!.")
            continue
        
        if position <0 or position >8:
            print("Invalid position!")
            continue
        
        if board[position]!="":
            print("That position is already occupied!")
            continue
        
        board[position]="X"
        
        if check_winner("X"):
            display_board()
            print("🎉 You win!")
            break
        
        if check_draw():
           display_board()
           print("It's a draw!")
           break
       
        print("Computer is thinking...!")
        computer_move()
        
        if check_winner("0"):
           display_board()
           print("❌ Computer wins!")
           break
       
        if check_draw():
           display_board()
           print("It's a draw!")
           break
       
       
       
play_game()