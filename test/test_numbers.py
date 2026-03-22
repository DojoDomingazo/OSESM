from src.numbers import average, median, normalize

# Test cases for numbers.py

# Test for wrong input types

def test_average_none():
    with pytest.raises(TypeError):
        average(None)

def test_average_string():
    with pytest.raises(TypeError):
        average("hola")

def test_average_mixed_types():
    with pytest.raises(TypeError):
        average([1, "dos", 3])

def test_average_with_none_inside():
    with pytest.raises(TypeError):
        average([1, None, 3])

def test_median_none():
    with pytest.raises(TypeError):
        median(None)

def test_normalize_none():
    with pytest.raises(TypeError):
        normalize(None)

def test_normalize_mixed_types():
    with pytest.raises(TypeError):
        normalize([1, "dos", 3])

# Average
def test_average_single():
    assert average([5]) == 5

def test_average_negatives():
    assert average([-2, -4]) == -3

def test_average_empty():
    with pytest.raises(ValueError):
        average([])

def test_average():
    assert average([1, 2, 3]) == 2
    assert average([10, 20]) == 15

# Median

def test_median():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([7]) == 7

def test_median_negatives():
    assert median([-3, -1, -2]) == -2

def test_median_duplicates():
    assert median([2, 2, 2, 3]) == 2

def test_median_empty():
    with pytest.raises(ValueError):
        median([])

# Normalize

def test_normalize():
    assert normalize([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize([5, 5, 5]) == [0.5, 0.5, 0.5]

def test_normalize_single():
    assert normalize([42]) == [0.5]

def test_normalize_negatives():
    assert normalize([-10, 0, 10]) == [0.0, 0.5, 1.0]

def test_normalize_empty():
    with pytest.raises(ValueError):
        normalize([])