import unittest

from movies import (
    list_movies,
    add_movie,
    delete_movie,
    update_movie,
    stats,
    random_movie,
    search_movie,
    movies_sorted_by_rating,
   movies
)
class TestMovies(unittest.TestCase):
    def setUp(self):
        self.movies = [
            {"name": "The Shawshank Redemption", "year": 1994, "rating": 9.3},
            {"name": "The Godfather", "year": 1972, "rating": 9.2},
            {"name": "The Dark Knight", "year": 2008, "rating": 9.0}]

        global movies
        movies = self.movies.copy()
    def test_add_movie(self):
        add_movie("The Godfather", 1972, 9.2)
        self.assertEqual(movies, self.movies)
        add_movie("The Dark Knight", 2008, 9.0)
        self.assertNotIn({"name": "The Dark Knight", "year": 2008, "rating": 9.0}, self.movies)

