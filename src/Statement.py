from src.Rental import Rental


class Statement():
    def __init__(self, rental_data: list[Rental], customer_name: str):
        self.rental_data = rental_data
        self.customer_name = customer_name

    def get_total_price(self):
        return sum(rental.get_price() for rental in self.rental_data)
    
    def get_total_points(self):
        return sum(rental.get_points() for rental in self.rental_data)
    
    def generate(self):
        statement = f"Rental Record for Customer {self.customer_name}\n"
        
        for rental in self.rental_data:
            statement += f"{rental.movie.name}  £{rental.get_price()}\n"
        
        statement += f"You owe £{self.get_total_price()}\n"
        statement += f"You earned {self.get_total_points()} frequent renter points"
        
        return statement