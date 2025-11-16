"""Plan: Dict prüfen Ziel>Ausgabe Bool ob Position gültig oder ungültig
Execute
Learning: In func isValidChessBoard we set the parameter board > and define it as a dict with strings as keys, then we loop through 
the iterable version created with the x.items() function > parameter board = provided dictionary (test_data)
"""
def isValidChessBoard(board: dict[str, str]) -> bool:
    valid_positions = {
    "a1","a2","a3","a4","a5","a6","a7","a8",
    "b1","b2","b3","b4","b5","b6","b7","b8",
    "c1","c2","c3","c4","c5","c6","c7","c8",
    "d1","d2","d3","d4","d5","d6","d7","d8",
    "e1","e2","e3","e4","e5","e6","e7","e8",
    "f1","f2","f3","f4","f5","f6","f7","f8",
    "g1","g2","g3","g4","g5","g6","g7","g8",
    "h1","h2","h3","h4","h5","h6","h7","h8"
}

    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    piece_counts = {
        'w': {'total': 0, 'pawn': 0, 'king': 0},
        'b': {'total': 0, 'pawn': 0, 'king': 0}
    }
    invalid_pos = 0
    valid_pos = 0
    for position, piece in board.items():
        if position == valid_positions:
            valid_pos += 1
        else:
            invalid_pos += 1

        if piece == valid_pieces:


        color = piece[0]
        name = piece[1:]

        # Zähle die Figuren
        #len(yourdict.keys())

    # Regeln prüfen
    for color in 'wb':
        if (piece_counts[color]['total'] > 16 or
            piece_counts[color]['pawn'] > 8 or
            piece_counts[color]['king'] != 1):
            return False

    return True

# Test mit dem Beispiel-Board
test_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
isValidChessBoard(test_board)