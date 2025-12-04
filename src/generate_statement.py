from src.calc_utils import GET_POINTS, GET_PRICE


def generate_statement(rental_data, customer_name):
    # Get price per rental
    # Get Total price of all
    # Get number of frequent renter points
    statement = ""

    total_price = 0.0
    renter_points = 0

    statement += f"Rental Record for Customer {customer_name}\n"
    
    for rental in rental_data:
        price = GET_PRICE[rental["type"]](rental["length"])
        renter_points += GET_POINTS[rental["type"]](rental["length"])

        total_price += price
        
        statement += f"{rental['name']}  £{price}\n"
    
    statement += f"You owe £{total_price}\n"
    statement += f"You earned {renter_points} frequent renter points"
    
    return statement