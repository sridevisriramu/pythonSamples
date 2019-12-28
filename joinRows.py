"""
Printing Pretty
We�re getting pretty close to a playable board, but wouldn�t it be nice to get rid of those quote marks and commas? We�re storing our data as a list, but the player doesn�t need to know that!

letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)
In the example above, we create a list called letters.
Then, we print a b c d. The .join method uses the string to combine the items in the list.
Finally, we print a---b---c---d. We are calling the .join function on the "---" string.
We want to turn each row into "O O O O O".

"""




board=[]
for i in range(1,6):
 board.append(["O"]*5)


def print_board(board_in):
 for row in board:
  print  " ".join(row)
  
print_board(board)  