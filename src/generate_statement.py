from src.Movie import Movie
from src.Rental import Rental
from src.Statement import Statement
from src.calc_utils import GET_POINTS, GET_PRICE


def generate_statement(rental_data: list[Rental], customer_name):
    return Statement(rental_data=rental_data, customer_name=customer_name).generate_text_statement()