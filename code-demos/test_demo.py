from demo import calculate_average

def test_normal():
    assert calculate_average([10, 20, 30]) == 20

def test_empty_list():
    try:
        calculate_average([])
        assert False, "Should have raised error"
    except ValueError:
        assert True

def test_single_number():
    assert calculate_average([50]) == 50
