

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            print("W", end=" ")
        else:
            print("B", end=" ")
    print()

# Chessboard with all pieces in correct starting positions

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],  # black pieces
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],  # white pawns
    ["R", "N", "B", "Q", "K", "B", "N", "R"]   # white pieces
]

print("Chess Board:")
for row in board:
    print(" ".join(row))
