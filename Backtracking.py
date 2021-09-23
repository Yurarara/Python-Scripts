
# Backtracking is an application of recursion. It allows for finding the optimal solution to a complex problem. If the
# algorithm finds out that a test solution cannot result in a viable final solution, it backtracks, discards the
# solution and continue with other solutions.

# An realisation of backtracking is the Eight Queens problem. There are 4,426,165,368 possible ways of positioning 8
# queens on a chess board, and the problem aims to find the placement of the queens so that none of them can attack the
# others. It's purely impractical to bruteforce it.
def is_legal(spot_taken):
    col = []
    row = []
    for ncol in range(8):
        for nrow in range(8):
            if spot_taken[ncol][nrow]:
                col.append(ncol)
                row.append(nrow)
    for i in range(len(col)-1):
        for j in range(i+1, len(col)):
            if row[i] == row[j] or col[i] == col[j]:
                return False
            if abs(row[i] - row[j]) == abs(col[i] - col[j]):
                return False
    return True


def eight_queens(spot_taken, num_positioned):
    # check whether the solution is already illegal
    if not is_legal(spot_taken):
        return False
    # check if all 8 queens have been placed:
    if num_positioned == 8:
        return True
    # extend the partial solution, try all possible placement of the next queen
    for col in range(8):
        for row in range(8):
            # check if the position is taken. if not, place a new queen.
            if not spot_taken[col][row]:
                spot_taken[col][row] = True
                # recurse, check if this placement leads to a solution
                if eight_queens(spot_taken, num_positioned + 1):
                    return True
                # if not, retract the update
                spot_taken[col][row] = False
    # if the programme processes to this line but haven't find a solution, there is no possible solution.
    return False


def print_spots(spot_taken):
    col = []
    row = []
    for ncol in range(8):
        for nrow in range(8):
            if spot_taken[ncol][nrow]:
                col.append(ncol)
                row.append(nrow)
    for i in range(len(col)):
        print(str(col[i]) + ", " + str(row[i]) + "//")


test_spots = []
for ite in range(0, 8):
    test_spots.append([False] * 8)
# print(eight_queens(test_spots, 0))
# print_spots(test_spots)


# Recursion can also be used on solving the Knight's Tour problem. The aim of this problem is to have a knight visiting
# all grids on a chess board without repeat. If the knight ends the tour in a grid next to the starting point, the route
# is considered closed, and the knight can start a tour at once.
# The basic idea is to move the knight to the grid (col, row) and recursively try out other moves.
def knights_tour(col, row, move_number, num_taken):
    # move the knight to designated position
    num_taken += 1
    move_number[col][row] = num_taken
    # if the knight moved 64 steps, it visits all grids on the board.
    if num_taken == 25:
        return True
    # construct arrays for all legal moves
    d_col = [-2, -2, -1, 1, 2, 2, 1, -1]
    d_row = [-1, 1, 2, 2, 1, -1, -2, -2]
    for i in range(8):
        next_col = col + d_col[i]
        next_row = row + d_row[i]
        # check if the move is legal. if legal, move the knight and recursively try out following moves.
        # IMPORTANT: because the knight has so many possible ways of moving, the number of all potential routes on a
        # 8*8 board is 8^64, an unimaginable large value. Hence it's hardly possible to solve a 8*8 knight's tour.
        # Therefore, we use a 5*5 board for this example.
        if 0 <= next_col <= 4 and 0 <= next_row <= 4 and move_number[next_col][next_row] == 0:
            if knights_tour(next_col, next_row, move_number, num_taken):
                return True
    move_number[col][row] = 0
    # if the programme processes to this line but haven't find a solution, there is no possible solution.
    return False


test_grids = []
for ite in range(5):
    test_grids.append([0] * 5)
print(knights_tour(1, 1, test_grids, 0))
for r in test_grids:
    print(r)


