# Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

# There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first square of a chess board, with the number of grains doubling on each successive square.

# There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

# Write code that shows:
#   - how many grains were on a given square, and
#   - the total number of grains on the chessboard

# Chess number  :   1   2   3   4   5   6   7   8   9   10  11  ...
# Grains        :   1   2   4   8   16  32  64  128 256 512 1024...

# Number of rice on a given square can be given by f(n) = 2^(n-1), when n is the box number.
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


# The total number of rice on the chess board is therefore 2^64 - 1.
def total():
    return 2 ** 64 - 1
