

def generate_statement(rental_data, customer_name):
    # Get price per rental
    # Get Total price of all
    # Get number of frequent renter points
    statement = ""

    total_price = 0.0
    renter_points = 0

    statement += f"Rental Record for Customer {customer_name}\n"
    
    for rental in rental_data:
        if(rental["type"] == "regular"):
            price = 2.0 if rental["length"] <= 2 else (rental["length"] - 2) * 1.50 + 2.0
            renter_points += 1
        elif(rental["type"] == "new"):
            price = rental["length"] * 3.0
            renter_points += 2 if rental["length"] >= 2 else 1
        else:
            price = 1.50 if rental["length"] <= 3 else (rental["length"] - 3) * 1.50 + 1.50
            renter_points += 1

        total_price += price
        
        statement += f"{rental['name']}  £{price}\n"
    
    statement += f"You owe £{total_price}\n"
    statement += f"You earned {renter_points} frequent renter points"
    
    return statement