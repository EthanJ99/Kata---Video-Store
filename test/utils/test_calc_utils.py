from src.utils.calc_utils import get_child_points, get_child_price, get_new_points, get_new_price, get_regular_points, get_regular_price


def test_get_regular_price():
    assert get_regular_price(1) == 2.0
    assert get_regular_price(3) == 3.5
    
def test_get_new_price():
    assert get_new_price(1) == 3.0
    assert get_new_price(3) == 9.0

def test_get_child_price():
    assert get_child_price(1) == 1.5
    assert get_child_price(3) == 1.5
    assert get_child_price(4) == 3.0

def test_get_regular_points():
    assert get_regular_points(1) == 1
    assert get_regular_points(5) == 1

def test_get_new_points():
    assert get_new_points(1) == 1
    assert get_new_points(5) == 2

def test_get_child_points():
    assert get_child_points(1) == 1
    assert get_child_points(5) == 1