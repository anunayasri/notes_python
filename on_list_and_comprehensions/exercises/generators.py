"""Generator Exercises."""


def is_prime(number):
    """Return True if candidate number is prime."""
    if number == 2:
        return True
    return not any(number%n == 0 for n in range(2,number))


def all_together(*list_of_iterables):
    """String together all items from the given iterables."""
    return (item for iterable in list_of_iterables for item in iterable)


def interleave(iter1, iter2):
    """Return iterable of one item at a time from each list."""
    return (item for pair in zip(iter1, iter2) for item in pair)


def translate(sentence):
    """Return a transliterated version of the given sentence."""
    dictionary = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return " ".join(dictionary[word] for word in sentence.split())


def parse_ranges(ranges):
    """Return a list of numbers corresponding to number ranges in a string"""
    list_of_ranges = []
    for num_range in ranges.split(','):
        start, end = num_range.split('-')
        start, end = int(start), int(end)
        list_of_ranges.append(range(start, end+1))

    return (item for range_entry in list_of_ranges for item in range_entry)
        

def first_prime_over():
    """Return the first prime number over a given number."""


def is_anagram():
    """Return True if the given words are anagrams."""
