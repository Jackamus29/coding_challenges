"""
This module solves the second challenge that
asks for all potential board positions a chess piece can advance to
given the name of the chess piece and its current position.
"""
import argparse
from itertools import permutations

col_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col_mapper = {
    l: i+1 for (i, l) in enumerate(col_letters)
}
chessboard = [
    ["%s%d" % (k, r) for r in range(1, 9)]
    for k in sorted(col_letters)
]


def bishop_potential_moves(cur_col, cur_row):
    """
    Builds and returns the list of potential positions for the bishop.
       Keyword Args:
        cur_col - int that represents the piece's current column (a-h).
        cur_row - int that represents the piece's current row (1-8).
    """
    potential_moves = []
    directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    for d in directions:
        temp_col, temp_row = cur_col + d[0], cur_row + d[1]
        while ((temp_col >= 0 and temp_col < 8) and
               (temp_row >= 0 and temp_row < 8)):
            potential_moves.append(chessboard[temp_col][temp_row])
            temp_col += d[0]
            temp_row += d[1]

    return potential_moves


def rook_potential_moves(cur_col, cur_row):
    """
    Builds and returns the list of potential positions for the rook.
       Keyword Args:
        cur_col - int that represents the piece's current column (a-h).
        cur_row - int that represents the piece's current row (1-8).
    """
    # concats two lists: one from the same column, and one from the same row.
    # it excludes the current position from both lists.
    return (
        [chessboard[cur_col][j] for j in range(8) if j != (cur_row)] +
        [chessboard[i][cur_row] for i in range(8) if i != (cur_col)]
    )


def queen_potential_moves(cur_col, cur_row):
    """
    Builds and returns the list of potential positions for the queen.
       Keyword Args:
        cur_col - int that represents the piece's current column (a-h).
        cur_row - int that represents the piece's current row (1-8).
    """
    # Queen's move set is the combination of the Rook's and Bishop's.
    return (
        bishop_potential_moves(cur_col, cur_row) +
        rook_potential_moves(cur_col, cur_row)
    )


def knight_potential_moves(cur_col, cur_row):
    """
    Builds and returns the list of potential positions for the knight.
       Keyword Args:
        cur_col - int that represents the piece's current column (a-h).
        cur_row - int that represents the piece's current row (1-8).
    """
    # list of possible movements for the knight
    # built from a permutation and filtered to movements of length 3
    movement_vectors = [
        (x, y) for (x, y)
        in permutations([-1, 1, -2, 2], 2)
        if (abs(x) + abs(y) == 3)
    ]

    return [
        # add the positions to the result list
        chessboard[i][j] for (i, j) in [
            # apply the movements to the current position
            ((cur_col + x), (cur_row + y))
            for (x, y) in movement_vectors
        ] if (  # only include in solution if within bounds
            (i >= 0 and i < len(chessboard)) and
            (j >= 0 and j < len(chessboard))
        )
    ]

movement_mapper = {
    "QUEEN": queen_potential_moves,
    "ROOK": rook_potential_moves,
    "BISHOP": bishop_potential_moves,
    "KNIGHT": knight_potential_moves
}


def chessercise(chess_piece, board_position):
    """
    Main function to import.
    Takes the name of the chess piece (e.g. ROOK)
    and the current position of the piece (e.g. d2)
    """
    col, row = list(board_position)
    return movement_mapper[chess_piece.upper()](
        cur_col=col_mapper[col]-1,
        cur_row=int(row)-1
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-piece")
    parser.add_argument("-position")
    args = parser.parse_args()
    piece, position = (args.piece, args.position)
    if piece is None or position is None:
        print "\tBoth PIECE and POSITION arguments are required."
        print "\tUse '--help' if needed."
        exit()
    print ", ".join(chessercise(piece, position))
