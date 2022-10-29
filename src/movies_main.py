import sys

from QueryManagement import QueryManager
from ReadData import ReadData
from timeit import timeit as timer


def main():
    """ reading movies and ratings using ReadData class and running all queries based on the all redirected input queries using QueryManager Class"""

    start=timer()
    data_reader = ReadData(small_data_movies="data/small.basics.tsv",small_data_ratings="data/title.ratings.tsv",large_data_movies="data/title.basics.tsv",large_data_ratings="data/title.ratings.tsv")
    if sys.argv[-1]=="small":
        movies_file=data_reader.small_data_movies
        ratings_file=data_reader.small_data_ratings
    else:
        movies_file = data_reader.large_data_movies
        ratings_file = data_reader.large_data_ratings
    print(f"reading {movies_file} into dict...")
    movies = data_reader.read_movies(movies_file)
    elapsed = timer() - start
    print(f"elapsed time:{elapsed}")
    print()

    start = timer()
    print(f"reading {ratings_file} into dict...")
    ratings = data_reader.read_ratings(ratings_file)
    elapsed = timer() - start
    print(f"elapsed time:{elapsed}")
    print()

    print(f"Total movies: {len(movies)}")
    print(f"Total ratings: {len(ratings)}")
    print()

    query_manager = QueryManager(movies, ratings)


    for line in sys.stdin:
        line = line.strip()   # remove trailing newline
        print(line)
        if 'LOOKUP' in line:
            tconst=line.split(" ")[1]
            query_manager.lookup(tconst)
        elif 'CONTAINS' in line:
            title_type=line.split(" ")[1]
            words=line.split(" ")[2:]
            words=" ".join(words)
            query_manager.contains(title_type,words)
        elif 'YEAR_AND_GENRE' in line:
            title_type,start_year,genres=line.split(" ")[1:]
            query_manager.year_genre(title_type,start_year,genres)
        elif 'RUNTIME' in line:
            title_type,start_time,end_time=line.split(" ")[1:]
            query_manager.runtime(title_type,start_time,end_time)
        elif 'MOST_VOTES' in line:
            title_type,num=line.split(" ")[1:]
            query_manager.most_votes(title_type,num)
        elif 'TOP' in line:
            title_type,num,start_year,end_year=line.split(" ")[1:]
            query_manager.top(title_type,num,start_year,end_year)
        print()



if __name__ == '__main__':
    main()