# Input Specification
# Your program will read four integers, where each integer is in the range 1...8. The first two integers
# represent the starting position of the knight. The second two integers represent the final position
# of the knight.

# Output Specification
# Your program should output the minimum (non-negative integer) number of moves required to
# move the knight from the starting position to the final position. Note that the knight is not allowed
# to move off the board during the sequence of moves.

start = [int(i) for i in input().split()]
end = [int(i) for i in input().split()]

def possible_moves(x, y):
    moves = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2)]
    to_remove = []
    for move in moves:
        if move[0] not in range(1, 9):
            to_remove.append(move)
        if move[1] not in range(1, 9):
            to_remove.append(move)
    moves = [move for move in moves if move not in to_remove]   
    return moves

def knight(start, end):
    num_moves = 1
    next_values = []
    start = tuple(x for x in start)
    end = tuple(x for x in end)
    x, y = start
    current = start
    moves_to_check = possible_moves(x, y)
    moves_checked = [tuple(i for i in current)]
    while True:
        if current == end:
            return 0
        if end in moves_to_check:
            return num_moves
        else:
            for i in moves_to_check:
                x, y = i
                search = possible_moves(x, y)
                moves_checked.append(tuple(x for x in i))
                for i in search:
                    if i not in moves_checked:
                        next_values.append(tuple(x for x in i))
        moves_to_check = set(next_values)
        num_moves += 1

print(knight(start, end))
    
