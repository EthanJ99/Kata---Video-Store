from src.Movie import Movie
from src.Rental import Rental
from src.Statement import Statement

def test_generate_statement_for_one_regular_rental():
    rental_data = [
        Rental(Movie("Crazynotes", "regular"), 1)
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £2.0\n"
        "You owe £2.0\n"
        "You earned 1 frequent renter points"
    )

    assert Statement(rental_data=rental_data, customer_name="Name").generate() == expected_statement


def test_generate_statement_for_three_regular_rentals():
    rental_data = [
        Rental(Movie("Crazynotes", "regular"), 1),
        Rental(Movie("Teeth", "regular"), 2),
        Rental(Movie("The Web", "regular"), 3)
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £2.0\n"
        "Teeth  £2.0\n"
        "The Web  £3.5\n"
        "You owe £7.5\n"
        "You earned 3 frequent renter points"
    )

    assert Statement(rental_data=rental_data, customer_name="Name").generate() == expected_statement

def test_generate_statement_for_one_new_rental():
    rental_data = [
        Rental(Movie("Crazynotes", "new"), 1)
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £3.0\n"
        "You owe £3.0\n"
        "You earned 1 frequent renter points"
    )

    assert Statement(rental_data=rental_data, customer_name="Name").generate() == expected_statement

def test_generate_statement_for_three_new_rentals():
    rental_data = [
        Rental(Movie("Crazynotes", "new"), 1),
        Rental(Movie("Teeth", "new"), 2),
        Rental(Movie("The Web", "new"), 3)  
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £3.0\n"
        "Teeth  £6.0\n"
        "The Web  £9.0\n"
        "You owe £18.0\n"
        "You earned 5 frequent renter points"
    )

    assert Statement(rental_data=rental_data, customer_name="Name").generate() == expected_statement

def test_generate_statement_for_one_childrens_rental():
    rental_data = [
        Rental(Movie("Crazynotes", "child"), 1)
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £1.5\n"
        "You owe £1.5\n"
        "You earned 1 frequent renter points"
    )

    assert Statement(rental_data=rental_data, customer_name="Name").generate() == expected_statement


def test_generate_statement_for_three_childrens_rentals():
    rental_data = [
        Rental(Movie("Crazynotes", "child"), 1),
        Rental(Movie("Teeth", "child"), 3),
        Rental(Movie("The Web", "child"), 4)  
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £1.5\n"
        "Teeth  £1.5\n"
        "The Web  £3.0\n"
        "You owe £6.0\n"
        "You earned 3 frequent renter points"
    )

    assert Statement(rental_data=rental_data, customer_name="Name").generate() == expected_statement
