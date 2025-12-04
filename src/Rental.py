from src import Movie
from src.utils.calc_utils import GET_POINTS, GET_PRICE


class Rental():
    def __init__(self, movie: Movie, length: int):
        self.movie = movie
        self.length = length

    def get_price(self):
        return GET_PRICE[self.movie.category](self.length)
    
    def get_points(self):
        return GET_POINTS[self.movie.category](self.length)