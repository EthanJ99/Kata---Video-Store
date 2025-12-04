from src.generate_statement import generate_statement


def test_generate_statement_for_three_regular_rentals():
    rental_data = [
        {"name": "Crazynotes", "length": 1, "type": "regular"},
        {"name": "Teeth", "length": 2, "type": "regular"},
        {"name": "The Web", "length": 3, "type": "regular"},
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £2.0\n"
        "Teeth  £2.0\n"
        "The Web  £3.5\n"
        "You owe £7.5\n"
        "You earned 3 frequent renter points"
    )

    assert generate_statement(rental_data=rental_data, customer_name="Name") == expected_statement

def test_generate_statement_for_one_new():
    rental_data = [
        {"name": "Crazynotes", "length": 1, "type": "new"}
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £3.0\n"
        "You owe £3.0\n"
        "You earned 1 frequent renter points"
    )

    assert generate_statement(rental_data=rental_data, customer_name="Name") == expected_statement

def test_generate_statement_for_three_new_rentals():
    rental_data = [
        {"name": "Crazynotes", "length": 1, "type": "new"},
        {"name": "Teeth", "length": 2, "type": "new"},
        {"name": "The Web", "length": 3, "type": "new"},
    ]

    expected_statement = (
        "Rental Record for Customer Name\n"
        "Crazynotes  £3.0\n"
        "Teeth  £6.0\n"
        "The Web  £9.0\n"
        "You owe £18.0\n"
        "You earned 5 frequent renter points"
    )

    assert generate_statement(rental_data=rental_data, customer_name="Name") == expected_statement

