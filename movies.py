
# list of the movies
movies = [
    {"name": "In the Name of the Father", "year": 1993, "rating": 8.1},
    {"name": "Titanic", "year": 1997, "rating": 7.9},
    {"name": "The Shawshank Redemption", "year": 1994, "rating": 9.3},
    {"name": "The Godfather", "year": 1972, "rating": 9.2},
    {"name": "The Dark Knight", "year": 2008, "rating": 9.0},
    {"name": "Schindler's List", "year": 1993, "rating": 8.9},
    {"name": "Forrest Gump", "year": 1994, "rating": 8.8},
    {"name": "Pulp Fiction", "year": 1994, "rating": 8.9},
    {"name": "The Matrix", "year": 1999, "rating": 1.0},
    {"name": "Fight Club", "year": 1999, "rating": 8.8},
]

#display the list of movies
def list_movies(movies):
    print(f"{len(movies)} movies in total")
    for movie in movies:
        print(f"Name: {movie['name']}, Year: {movie['year']}, Rating: {movie['rating']}")

# add a movie to the list
def add_movie():
    name = str(input("Enter the name of the movie: ")).lower().strip()
    year = int(input("Enter the year of the movie: "))
    rating = float(input("Enter the rating of the movie: "))
    movie = {"name": name, "year": year, "rating": rating}
    movies.append(movie)








def menu():
    print(
        """
        ***************** Welcome to the Movie App *****************
         
        Menu:
        0. Exit
        1. List movies
        2. add movie
        3.Delete movie
        4.Update move
        5.Stats
        6.Randome movie
        7.Search movie
        8.Movies sorted by rating
        9.Movies sorted by year
        10. Filter movies
        
        Enter choise (0-10):
        """
    )
    add_movie()
    list_movies(movies)











def main():
    menu()

if __name__ == "__main__":
    main()