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

    def contains(self,title_type,words):
        """: Find all movies of a certain type whose titles contain the sequence of words.
         :param filename: title_type,words
         prints movies results
         """
        start = timer()
        movie_found = False
        for movie in self.movies:
            if movie.titleType==title_type and words in movie.primaryTitle:
                print(f"processing: CONTAINS {title_type} {words}")
                print(f"Identifier: {movie.tconst}, Title: {movie.primaryTitle}, Type: {movie.titleType}, Year: {movie.startYear},Runtime: {movie.runtimeMinutes}, Genres: {movie.genres}")
        if not movie_found:
            print(f"processing: CONTAINS {title_type} {words}\nNo match found!")
        elapsed = timer() - start
        print(f"elapsed time:{elapsed}")

    def year_genre(self,title_type,year,genres):
        """: : Find all movies of a certain type from a particular year that match a genre.
         :param filename: title_type,year,genres
         prints movies results
                 """

        start = timer()
        movies_results=[]
        for movie in self.movies:
            if movie.titleType == title_type and movie.startYear==year and movie.genres==genres:
                movies_results.append(movie)

        if movies_results:
            movies_results.sort(key=operator.attrgetter('primaryTitle'))

            print(f"processing: YEAR_AND_GENRE {title_type} {year} {genres}")
            for movie in movies_results:
                print(
                f"Identifier: {movie.tconst}, Title: {movie.primaryTitle}, Type: {movie.titleType}, Year: {movie.startYear},Runtime: {movie.runtimeMinutes}, Genres: {movie.genres}")
        else:
            print(f"processing: YEAR_AND_GENRE {title_type} {year} {genres}\nNo match found!")
        elapsed = timer() - start
        print(f"elapsed time:{elapsed}")