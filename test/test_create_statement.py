from src.generate_statement import VideoStore, generate_statement


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

    assert VideoStore(rental_data, "Customer Name").generate_statement() == expected_statement

