from src.Movie import Movie
from src.Rental import Rental
from src.calc_utils import GET_POINTS, GET_PRICE


def generate_statement(rental_data: list[Rental], customer_name):
    # Get price per rental
    # Get Total price of all
    # Get number of frequent renter points
    statement = ""

    total_price = 0.0
    renter_points = 0

    statement += f"Rental Record for Customer {customer_name}\n"
    
    for rental in rental_data:
        price = rental.get_price()
        renter_points += rental.get_points()

        total_price += price
        
        statement += f"{rental.movie.name}  £{price}\n"
    
    statement += f"You owe £{total_price}\n"
    statement += f"You earned {renter_points} frequent renter points"
    
    return statement