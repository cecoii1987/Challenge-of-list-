In_board = ["---##",

         "-#---",

         "--#--",

         "-##--",

         "-----"]

offs = [ (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1) ]

res  = [ [[0,"#"][c=="#"] for c in row] for row in In_board] # initialization of minesweeper

for r,s in enumerate(In_board):  # go through rows of minesweeper

    for c,m in enumerate(s):  # go through corresponding columns

        for dr,dc in [] if m=="#" else offs: # neighboring cells of "-" cells

            if r+dr in range(len(In_board)) and c+dc in range(len(s)):

                res[r][c] += In_board[r+dr][c+dc] == "#" # counting mines in array

                
for row in res:

    for c in row:

        print(c,end=" ")

    print()     #Printing a resulting array
