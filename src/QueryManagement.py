import operator
from timeit import default_timer as timer




class QueryManager:
    """ QueryManager class is responsible for running all queries"""
    def __init__(self,movies,ratings):
        self.movies =movies
        self.ratings=ratings

    def lookup(self,tconst):
        """: Look up a movie and rating by its unique identifier.
         :param filename: tconst id
         prints movies results
         """
        start=timer()
        movie_found=False
        rating_found=False
        for movie in self.movies:
            if movie.tconst==tconst:
              movie_found=True
              print(f"MOVIE: Identifier: {movie.tconst}, Title: {movie.primaryTitle}, Type: {movie.titleType}, Year: {movie.startYear},Runtime: {movie.runtimeMinutes}, Genres: {movie.genres}")

        for rating in self.ratings:
            if rating.tconst==tconst:
                rating_found=True
                print(f"RATING: Identifier: {rating.tconst}, Rating: {rating.averageRating}, Votes: {rating.numVotes}")
        elapsed=timer()-start

        if not (movie_found and rating_found):
            print(f"processing: LOOKUP {tconst}\nMovie not found!\nRating not found!")
        print(f"elapsed time:{elapsed}")