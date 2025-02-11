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
def list_movies():
    print(f"{len(movies)} movies in total")
    for movie in movies:
        print(f"Name: {movie['name']}, Year: {movie['year']}, Rating: {movie['rating']}")
    prompt("\nPress enter to continue")



# add a movie to the list
def add_movie():
    name = str(input("Enter the new movie name:  ")).lower().strip()
    year = int(input("Enter new movie year: "))
    while year < 1900 or year > 2025 and year != isinstance(int):
        year = int(input("Enter a valid year between 1900 and 2025: "))
    rating = float(input("Enter new movie rating: "))
    while rating < 0 or rating > 10 and rating != isinstance(float):
        rating = float(input("Enter a valid rating between 0 and 10: "))
    movie = {"name": name, "year": year, "rating": rating}
    movies.append(movie)
    print(f"{name} has been added to the list successfully")
    prompt("\nPress enter to continue")

#delete a movie from the list by name of the movie
def delete_movie():
    name = str(input("Enter movie name to delete: ")).lower().strip()
    for movie in movies:
        if movie["name"] == name:
            movies.remove(movie)
            print(f"{name} has been removed from the list")
        else :
            print(f"Movie {name} is not in the list")
    prompt("\nPress enter to continue")

# update a movie in the list
def update_movie():
    name = str(input("Enter movie name: ")).lower().strip()
    for movie in movies:
        if movie["name"] == name:
            rating = get_valid_rating()
            movie["rating"] = rating
            print(f"{name} has been updated")
        else:
            print(f"Movie {name} is not in the list")
    prompt("\nPress enter to continue")

#stats of the movies
def stats():
    total_movies = len(movies)
    total_rating = sum([movie["rating"] for movie in movies])
    avg_rating = total_rating / total_movies
    print(f"Average rating of the movies: {avg_rating}")
    print("Median rating of the movies: ", sorted([movie["rating"] for movie in movies])[len(movies) // 2])
    print("Best movie: ", max(movies, key=lambda movie: movie["rating"])["name"])
    print("Worst movie: ", min(movies, key=lambda movie: movie["rating"])["name"])
    prompt("\nPress enter to continue")

#random movie
def random_movie():
    movie = random.choice(movies)
    print(f"Name: {movie['name']}, Year: {movie['year']}, Rating: {movie['rating']}")
    prompt("\nPress enter to continue")

#Search for a part of the movie name
def search_movie():
    search = str(input("Enter the name of the movie you want to search: ")).lower().strip()
    for movie in movies:
        if search in movie["name"]:
            print(f"Name: {movie['name']}, Rating: {movie['rating']}")
        else:
            print(f"{search} is not in the list")
    prompt("\nPress enter to continue")

#movies sorted by rating
def movies_sorted_by_rating():
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    for movie in sorted_movies:
        print(f"Name: {movie['name']}, Rating: {movie['rating']}")
    prompt("\nPress enter to continue")



#movies sorted by year
def movies_sorted_by_year():
    sorted_movies = sorted(movies, key=lambda movie: movie["year"])
    for movie in sorted_movies:
        print(f"Name: {movie['name']}, Year: {movie['year']}")
    prompt("\nPress enter to continue")

#Enter minimum rating (leave blank for no minimum rating): 3
#Enter start year (leave blank for no start year): 2000
#Enter end year (leave blank for no end year): 2025
#The Dark Knight (2008): 9.0
#Four session  (2010): 3.0
#The Avengers (2012): 8.0

def filter_movies():
    min_rating = float(input("Enter minimum rating (leave blank for no minimum rating): ") or 0)
    start_year = int(input("Enter start year (leave blank for no start year): ") or 0)
    end_year = int(input("Enter end year (leave blank for no end year): ") or 9999)
    sorted_movies = sorted(movies, key=lambda movie: movie["year"])
    for movie in sorted_movies:
        if movie["rating"] >= min_rating and start_year <= movie["year"] <= end_year:
            print(f"{movie['name']} ({movie['year']}): {movie['rating']}")
    prompt("\nPress enter to continue")


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
        """
    )

#promptet to display the menu
def prompt(message):
    enter = input(message)
    return menu()
 #validator
def get_valid_rating():
    while True:
        try:
            rating = float(input("Enter a rating between 0 and 10: "))
            if 0 <= rating <= 10:
                return rating  # Valid rating, return it
            else:
                print("Invalid input! Rating must be between 0 and 10.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Now, you can just call the function wherever needed:



def main():
    menu()
    while True:
        choice = int(input("Enter your choice:(0-10): "))
        actions = {
            0: exit,
            1: list_movies,
            2: add_movie,
            3: delete_movie,
            4: update_movie,
            5: stats,
            6: random_movie,
            7: search_movie,
            8: movies_sorted_by_rating,
            9: movies_sorted_by_year,
            10: filter_movies
        }
        if choice == 0:
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")

if __name__ == "__main__":
    main()