# Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

# The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

# Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

# You are not expected to discover an efficient solution to this yourself from first principles; research is allowed, indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering.

def square_of_sum(N):
    sum = 0

    for i in range(1, N+1):
        sum += i
    
    return sum ** 2


def sum_of_squares(N):
    sos = 0

    for i in range(1, N+1):
        sos += i ** 2

    return sos


def difference_of_squares(N):
    return square_of_sum(N) - sum_of_squares(N)


# TESTS
N = 10

print("Square of Sum: {}".format(square_of_sum(N)))
print("Sum of Squares: {}".format(sum_of_squares(N)))
print("Difference of Squares: {}".format(difference_of_squares(N)))
