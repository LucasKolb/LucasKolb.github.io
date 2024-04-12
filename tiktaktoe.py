def display_board(board):
  row1 = " "
  if board[0] == "-":
    row1 += " "
  else:
    row1 += board[0]
  row1 += " | "

  if board[1] == "-":
    row1 += " "
  else:
    row1 += board[1] 
  row1 += " | "


  if board[2] == "-":
    row1 += " "
  else:
    row1 += board[2]


  print(row1)
  print("-----------")
  row2 = " "


  if board[3] == "-":
    row2 += " "
  else:
    row2 += board[3]
  row2 +=" | "


  if board[4] == "-":
    row2 += " "
  else:
    row2 += board[4]
  row2 += " | "


  if board[5] == "-":
    row2 += " "
  else:
    row2 += board[5]

  print(row2)
  print("-----------")
  row3 = " "


  if board[6] == "-":
    row3 += " "
  else:
    row3 += board[6]


  row3 += " | "

  if board[7] == "-":
    row3 += " "
  else:
    row3 += board[7]  


  row3 += " | "

  if board[8] == "-":
    row3 += " "
  else:
    row3 += board[8]  

  print(row3)

def make_move(board, player):

  played = False
  while played == False:
    user_Input = int(input("Your Move (0-8) for " + move + ": "))
    if user_Input < 0 or user_Input > 8:
      print(user_Input, "Can't move there, use only (0-8)")
    elif board[user_Input] != "-":
      print("Bro, Board", user_Input, "is already in use")
    else:
      board[ user_Input ] = player
      played = True
  # if has_a_win(board) == True:
  #   return False
  return board
    
def has_a_win(board):
  if board[0] != '-' and board[0] == board[3] and board[3] == board[6]:
    return True
  if board[1] != '-' and board[1] == board[4] and board[4] == board[7]:
    return True
  if board[2] != '-' and board[2] == board[5] and board[5] == board[8]:
    return True
  if board[0] != '-' and board[0] == board[1] and board[1] == board[2]:
    return True
  if board[3] != '-' and board[3] == board[4] and board[4] == board[5]:
    return True
  if board[6] != '-' and board[6] == board[7] and board[7] == board[8]:
      return True
  if board[0] != '-' and board[0] == board[4] and board[4] == board[8]:
    return True
  if board[2] != '-' and board[2] == board[4] and board[4] == board[6]:
    return True
def is_a_tie(board):
  if board[0] != '-' and board[1] != '-' and board[2] != '-' and board[3] != '-' and board[4] != '-' and board[5] != '-' and board[6] != '-' and board[7] != '-' and board[8] != '-':
    return True
  else:
    return False
# #
# TODO: Add functions and any other code you need.
# #


board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

move = 'X'
while True:
  display_board(board)
  make_move(board, move)
  if has_a_win(board):
    display_board(board)
    print (move + ", You won Cuh!")
    break
    
  if is_a_tie(board):
    display_board(board)
    print("Its a tie")
    break
  
  # Switch player
  if move == 'X': 
    move = 'O'
  else: 
    move = 'X'
