favorite_movies = ["movie_1", "movie_2", "movie_3", "movie_4", "movie_5"]

print("give a movie: ")
new_movie = input()

if new_movie in favorite_movies:
    print("there is already..")
else:
    favorite_movies.append(new_movie)
    favorite_movies.sort()
    print(favorite_movies)
    print(len(favorite_movies))