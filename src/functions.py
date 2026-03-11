""""
Basic functions to do things with numbers
"""

def average(numbers):
    if not numbers:
        raise ValueError ("The list can not be empty!")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError ("The list can not be empty!")
    sortedn = sorted(numbers)
    n = len(sortedn)
    hf = n // 2
    if n % 2 == 0:
        return (sortedn[hf - 1] + sortedn[hf]) / 2
    return sortedn[hf]

def normalize(numbers):
    if not numbers:
        raise ValueError ("The list can not be empty!")
    minimum = min(numbers)
    maximum = max(numbers)
    if minimum == maximum:
        return [0.5 for _ in numbers]
    return [(v - minimum) / (maximum - minimum) for v in numbers]