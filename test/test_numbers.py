from src.numbers import average, median, normalize

def test_average():
    assert average([1, 2, 3]) == 2
    assert average([10, 20]) == 15

def test_median():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([7]) == 7

def test_normalize():
    assert normalize([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize([5, 5, 5]) == [0.5, 0.5, 0.5]
