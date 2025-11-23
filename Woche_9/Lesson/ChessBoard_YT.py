"""Plan: Dict prüfen Ziel>Ausgabe Bool ob Position gültig oder ungültig
Execute
Learning: In func isValidChessBoard we set the parameter board > and define it as a dict with strings as keys, then we loop through 
the iterable version created with the x.items() function > parameter board = provided dictionary (test_data)
"""
def isValidChessBoard(board: dict[str, str]) -> bool:
    valid_positions = {
    "1a","2a","3a","4a","5a","6a","7a","8a",
    "1b","2b","3b","4b","5b","6b","7b","8b",
    "1c","2c","3c","4c","5c","6c","7c","8c",
    "1d","2d","3d","4d","5d","6d","7d","8d",
    "1e","2e","3e","4e","5e","6e","7e","8e",
    "1f","2f","3f","4f","5f","6f","7f","8f",
    "1g","2g","3g","4g","5g","6g","7g","8g",
    "1h","2h","3h","4h","5h","6h","7h","8h"
}

    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}

    piece_counts = {
        'w': {'total': 0, 'pawn': 0, 'king': 0},
        'b': {'total': 0, 'pawn': 0, 'king': 0}
    }
    invalid_pos = 0
    valid_pos = 0
    valid_pcs = 0
    invalid_pcs = 0
    for position, piece in board.items():
        if position in valid_positions:
            valid_pos += 1
        else:
            invalid_pos += 1

        if piece[1:] in valid_pieces:
            valid_pcs +=1
        else:
            invalid_pcs += 1
    # counting the pieces

        color = piece[0] #definiert farbe als 1. index von piece
        name = piece[1:] #definiert name des pieces als 1. Index bis ende von piece

        piece_counts[color]["total"] += 1

        if name == "pawn":
            piece_counts[color]["pawn"] += 1
        if name == "king":
            piece_counts[color]["king"] += 1

    # Regeln prüfen
    for color in 'wb':
        if (piece_counts[color]['total'] > 16 or
            piece_counts[color]['pawn'] > 8 or
            piece_counts[color]['king'] != 1):
            return False

    return True

# Test mit dem Beispiel-Board
test_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(test_board))