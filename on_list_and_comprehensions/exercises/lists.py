"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [name for name in names if name[0].lower() in 'aeiou']


def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    return [n**i for i, n in enumerate(numbers)]

def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [e for row in matrix for e in row]


def reverse_difference(l):
    """Return list subtracted from the reverse of itself."""
    return [x-y for x,y in zip(l, l[::-1])]


def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [e1 + e2 for e1, e2 in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
        
    ]


def transpose(matrix):
    """Return a transposed version of given list of lists."""
    return [list(row) for row in zip(*matrix)]


def get_factors(n):
    """Return a list of all factors of the given number."""
    return [i for i in range(n+1)[1:] if n%i==0]


def triples():
    """Return list of Pythagorean triples less than input num."""
