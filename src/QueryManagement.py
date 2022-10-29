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

    def runtime(self,title_type,start_time,end_time):
        """Find all movies of a certain type that are within a range of runtimes.
             :param filename:,title_type,start_time,end_time
             prints movies results
        """
        start = timer()
        movies_results = []
        for movie in self.movies:
            if movie.titleType == title_type and movie.runtimeMinutes >= start_time and movie.runtimeMinutes <= end_time:
                movies_results.append(movie)

        if movies_results:
            movies_results.sort(key=operator.attrgetter('primaryTitle'))
            movies_results.sort(key=operator.attrgetter('runtimeMinutes'),reverse=True)

            print(f"\nprocessing: RUNTIME {title_type} {start_time} {end_time}")
            for movie in movies_results:
                print(f"\tIdentifier: {movie.tconst}, Title: {movie.primaryTitle}, Type: {movie.titleType}, Year: {movie.startYear},Runtime: {movie.runtimeMinutes}, Genres: {movie.genres}")
        else:
            print(f"processing: RUNTIME {title_type} {start_time} {end_time}\nNo match found!")
        elapsed = timer() - start
        print(f"elapsed time:{elapsed}")

    def most_votes(self,title_type,num):
        """Find the given number of movies of a certain type with the most votes
         :param filename:,title_type,number of movies
         prints movies results """
        start = timer()
        movies_results = []
        movies_specified_title = []
        for movie in self.movies:
            if movie.titleType == title_type:
                for rating in self.ratings:
                    if rating.tconst == movie.tconst:
                        movie_dict=movie.__dict__
                        movie_dict["numVotes"]=rating.numVotes
                        movies_specified_title.append(movie_dict)
        if movies_specified_title:
            sorted_movies=sorted(movies_specified_title,key=lambda x:x['primaryTitle'])[:int(num)]
            sorted_movies=sorted(sorted_movies,key=lambda x:(int(x['numVotes'])),reverse=True)
            print(f"\nprocessing: MOST_VOTES {title_type} {num}")
            for index,movie in enumerate(sorted_movies,start=1):
                print(
                    f"\t{index}. VOTES: {movie['numVotes']}, MOVIE: Identifier: {movie['tconst']}, Title: {movie['primaryTitle']}, Type: {movie['titleType']}, Year: {movie['startYear']},Runtime: {movie['runtimeMinutes']}, Genres: {movie['genres']}")
        else:
            print(f"processing: MOST_VOTES {title_type} {num}\nNo match found!")
        elapsed = timer() - start
        print(f"elapsed time:{elapsed}")


    def top(self,title_type,num,start_year,end_year):
        """Find the number of movies of a certain type by a range of years (inclusive) that are the highest rated and have at
           least 1000 votes.
           :param title_type,num,start_year,end_year
           prints results"""
        start = timer()
        movies_specified = []

        for movie in self.movies:
            if movie.titleType == title_type and movie.startYear>=start_year and movie.endYear<=end_year:
                for rating in self.ratings:
                    if rating.tconst == movie.tconst and int(rating.numVotes)>=1000:
                        movie_dict = movie.__dict__
                        movie_dict["numVotes"] = rating.numVotes
                        movie_dict["rating"] = rating.averageRating
                        movies_specified.append(movie_dict)

        if movies_specified:
            sorted_by_year = sorted(movies_specified, key=lambda x: (int(x['startYear'])))
            print(f"\nprocessing: TOP {title_type} {num} {start_year} {end_year}")
            for year in range(int(start_year),int(end_year)+1):
                filtered_by_year_wise=filter(lambda x:int(x['startYear'])==int(year),list(sorted_by_year))
                if filtered_by_year_wise:
                    sorted_movies = sorted(movies_specified, key=lambda x: (float((x['numVotes']))),reverse=True)[:int(num)]
                    sorted_movies = sorted(sorted_movies, key=lambda x: (float(x['rating'])),reverse=True)
                    print(f"\tYEAR: {year}")
                    for index, movie in enumerate(sorted_movies, start=1):
                        print(
                            f"\t\t{index}. RATING: {movie['rating']}, VOTES: {movie['numVotes']}, MOVIE: Identifier: {movie['tconst']}, Title: {movie['primaryTitle']}, Type: {movie['titleType']}, Year: {movie['startYear']},Runtime: {movie['runtimeMinutes']}, Genres: {movie['genres']}")
        else:
            print(f"processing: MOST_VOTES {title_type} {num}\nNo match found!")
        elapsed = timer() - start
        print(f"elapsed time:{elapsed}")