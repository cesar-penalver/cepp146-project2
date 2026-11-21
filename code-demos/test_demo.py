from demo import calculate_average

def test_normal():
    # Normal case - should work
    assert calculate_average([10, 20, 30]) == 20

def test_empty_list():
    # Edge case - this is where the agent failed first
    try:
        result = calculate_average([])
        assert result == 0
    except ZeroDivisionError:
        assert False, "CRASHED on empty list - bug found"

def test_single_number():
    # One number - average should be that number
    assert calculate_average([50]) == 50
