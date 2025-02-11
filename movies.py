import random
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

#delete a movie from the list by name of the movie
def delete_movie():
    name = str(input("Enter the name of the movie you want to delete: ")).lower().strip()
    for movie in movies:
        if movie["name"] == name:
            movies.remove(movie)
            print(f"{name} has been removed from the list")
        else :
            print(f"{name} is not in the list")

# update a movie in the list
def update_movie():
    name = str(input("Enter the name of the movie you want to update: ")).lower().strip()
    for movie in movies:
        if movie["name"] == name:
            rating = float(input("Enter the new rating of the movie: "))
            movie["rating"] = rating
            print(f"{name} has been updated")
        else:
            print(f"{name} is not in the list")

#stats of the movies
def stats():
    total_movies = len(movies)
    total_rating = sum([movie["rating"] for movie in movies])
    avg_rating = total_rating / total_movies
    print(f"Total number of movies: {total_movies}")
    print(f"Total rating of the movies: {total_rating}")
    print(f"Average rating of the movies: {avg_rating}")
    print("Median rating of the movies: ", sorted([movie["rating"] for movie in movies])[len(movies) // 2])

#random movie
def random_movie():
    movie = random.choice(movies)
    print(f"Name: {movie['name']}, Year: {movie['year']}, Rating: {movie['rating']}")

#Search for a part of the movie name
def search_movie():
    search = str(input("Enter the name of the movie you want to search: ")).lower().strip()
    for movie in movies:
        if search in movie["name"]:
            print(f"Name: {movie['name']}, Rating: {movie['rating']}")
        else:
            print(f"{search} is not in the list")

#movies sorted by rating
def movies_sorted_by_rating():
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    for movie in sorted_movies:
        print(f"Name: {movie['name']}, Rating: {movie['rating']}")

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
    delete_movie()
    list_movies(movies)











def main():
    menu()

if __name__ == "__main__":
    main()