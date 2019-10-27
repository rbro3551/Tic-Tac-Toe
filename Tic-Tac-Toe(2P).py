def checkifwin():
   '''Tests if various combonations of three symbols in a row exist in the current game board'''
   l = len(bboard[0])
   diag = [bboard[i][i] for i in range(l)]
   diag2 = [bboard[i][i + 1] for i in range(3)]
   diag3 = [bboard[i + 1][i] for i in range(3)]
   revdiag = [bboard[l-1-i][i] for i in range(l-1,-1,-1)]
   revdiag2 = [bboard[l - 2 - i][i + 0] for i in range(l - 1)]
   revdiag3 = [bboard[l-1-i][i+1] for i in range(l-1)]
   row1 = [bboard[0][i] for i in range(l)]
   row2 = [bboard[1][i] for i in range(l)]
   row3 = [bboard[2][i] for i in range(l)]
   row4 = [bboard[3][i] for i in range(l)]
   column1 = [bboard[i][0] for i in range(l)]
   column2 = [bboard[i][1] for i in range(l)]
   column3 = [bboard[i][2] for i in range(l)]
   column4 = [bboard[i][3] for i in range(l)]
   if diag.count(p1char) == 3 or diag.count(p2char) == 3:
      return True
   elif diag2.count(p1char) == 3 or diag2.count(p2char) == 3:
      return True
   elif diag3.count(p1char) == 3 or diag3.count(p2char) == 3:
      return True
   elif revdiag.count(p1char) == 3 or revdiag.count(p2char) == 3:
      return True
   elif revdiag2.count(p1char) == 3 or revdiag2.count(p2char) == 3:
      return True
   elif revdiag3.count(p1char) == 3 or revdiag3.count(p2char) == 3:
      return True
   elif row1.count(p1char) == 3 or row1.count(p2char) == 3:
      return True
   elif row2.count(p1char) == 3 or row2.count(p2char) == 3:
      return True
   elif row3.count(p1char) == 3 or row3.count(p2char) == 3:
      return True
   elif row4.count(p1char) == 3 or row4.count(p2char) == 3:
      return True
   elif column1.count(p1char) == 3 or column1.count(p2char) == 3:
      return True
   elif column2.count(p1char) == 3 or column2.count(p2char) == 3:
      return True
   elif column3.count(p1char) == 3 or column3.count(p2char) == 3:
      return True
   elif column4.count(p1char) == 3 or column4.count(p2char) == 3:
      return True
   else:
      return False

def player1():
   '''Receives input from player 1 on where to put their symbol and places the symbol'''
   while True:
      try:
         while True:
            p1pos1 = int(input('Enter the row number [1 to 4]'))
            p1pos2 = int(input('Enter the column number [1 to 4]'))
            if bboard[p1pos1 - 1][p1pos2 - 1] != '-':
               print('Choose an empty space')
               continue
            else:
               break
         bboard[p1pos1 - 1][p1pos2 - 1] = p1char
         break
      except ValueError:
         print('Input must be valid')
      except IndexError:
         print('Input must be in range 1-4')

def player2():
   '''Receives input from player 2 on where to put their symbol and places the symbol'''
   while True:
      try:
         while True:
            p2pos1 = int(input('Enter the row number [1 to 4]'))
            p2pos2 = int(input('Enter the column number [1 to 4]'))
            if bboard[p2pos1 - 1][p2pos2 - 1] != '-':
               print('Choose an empty space')
               continue
            else:
               break
         bboard[p2pos1 - 1][p2pos2 - 1] = p2char
         break
      except ValueError:
         print('Input must be valid')
      except IndexError:
         print('Input must be in range 1-4')

p1name = input('Enter Player 1 name:')
p2name = input('Enter Player 2 name:')          #Input player info
p1char = input('Enter Player 1 symbol:')
p2char = input('Enter Player 2 symbol:')
bboard = (['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'])
while True:
   print(' '.join(bboard[0]))
   print(' '.join(bboard[1]))
   print(' '.join(bboard[2]))          #Display board every turn
   print(' '.join(bboard[3]))
   print('%s\'s turn:' %(p1name))
   player1()
   if checkifwin() == True:
      print('%s is a wiener' % p1name)          #Check if either player has won after every placement
      break
   else:
      pass
   print(' '.join(bboard[0]))
   print(' '.join(bboard[1]))
   print(' '.join(bboard[2]))
   print(' '.join(bboard[3]))
   print('%s\'s turn' % p2name)
   player2()
   if checkifwin() == True:
      print('%s is a wiener' % p2name)
      break
   else:
      continue
print(' '.join(bboard[0]))
print(' '.join(bboard[1]))
print(' '.join(bboard[2]))          #Display winning board
print(' '.join(bboard[3]))