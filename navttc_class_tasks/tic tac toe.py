import random

#Test

board=["--" , "--" , "--",
       "--" , "--" , "--",
       "--" , "--" , "--"]

currnt_player="x"
winner=None
gamerunning=True


#printing the game board
def printboard(board):
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print("----------")
    print(board[3] + "|" + board[4] + "|" +board[5])
    print("----------")
    print(board[6] + "|" + board[7] + "|" + board[8])
#take player input


def playerinput (board):
    user_input=int(input("enter the number fron 1 to 9:"))
    if user_input>=1 and user_input<=9 and board[user_input-1]=="--":
        board[user_input-1]=currnt_player
    else:
        print("sorry player is already in that spot!")

# check for win or tie
def checkhorizontal (board):
    global winner
    if board[0]== board[1]== board[2] and board[0]!="--":
        winner= board[0]
        return True
    elif board[3]== board[4]== board[5] and board[3]!="--":
        winner= board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "--":
        winner = board[6]
        return True


def check_row (board):
    global winner
    if board[0]== board[3]== board[6] and board[0]!="--":
        winner= board[0]
        return True
    elif board[1]== board[4]== board[7] and board[1]!="--":
        winner= board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "--":
        winner = board[2]
        return True

def check_diagnol (board):
    global winner
    if board[0]== board[4]== board[8] and board[0]!="--":
        winner= board[0]
        return True
    elif board[2]== board[4]== board[6] and board[2]!="--":
        winner= board[2]
        return True
# check for tie
def chech_Tie(board):
    global gamerunning
    if "--" not in board:
        printboard(board)
        print("It is a tie!")
        gamerunning=False



#switch the player

def switch_player():
    global currnt_player
    if currnt_player=="x":
        currnt_player="0"
    else:
        currnt_player="x"

#check for winner
def check_win():
    if check_diagnol(board)or check_row(board)or checkhorizontal(board):
        print("the winner is ",winner)


# def machine_com (board):
#     position= random.randint(0,8)
#     if board [position]=="--":
#         board[position]="0"
#         switch_player()

# check for win and try again

while gamerunning:
    printboard(board)
    playerinput(board)
    check_win()
    chech_Tie(board)
    switch_player()
    # machine_com(board)
    # check_win()
    # chech_Tie(board)