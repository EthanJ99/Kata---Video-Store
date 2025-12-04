def get_regular_price(length):
    return 2.0 if length <= 2 else (length - 2) * 1.50 + 2.0
    
def get_new_price(length):
    return length * 3.0

def get_child_price(length):
    return 1.50 if length <= 3 else (length - 3) * 1.50 + 1.50

def get_regular_points(length):
    return 1

def get_new_points(length):
    return 2 if length >= 2 else 1

def get_child_points(length):
    return 1

GET_PRICE = {
    "regular": get_regular_price,
    "new": get_new_price,
    "child": get_child_price
}

GET_POINTS = {
    "regular": get_regular_points,
    "new": get_new_points,
    "child": get_child_points
}