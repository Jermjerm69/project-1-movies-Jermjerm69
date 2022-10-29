from Movie import Movie
from Rating import Rating


class ReadData:
    """ ReadData class reads the data from Small and large movies dataset and ratings dataset"""
    def __init__(self,small_data_movies,small_data_ratings,large_data_movies,large_data_ratings):
        self.movies=[]
        self.ratings=[]
        self.small_data_movies=small_data_movies
        self.small_data_ratings=small_data_ratings
        self.large_data_movies=large_data_movies
        self.large_data_ratings=large_data_ratings

    def read_movies(self,file_name: str) -> list[Movie]:
        """
        Read movie from a file into a list of Movie dataclass objects.
        :param filename: The name of the file
        :return: A list of Movies
        """

        # opening movie file for reading purpose
        with open(file_name, encoding="utf-8") as f:
            # i=0
            for line in f.readlines():
                fields = line.split('\t')
                fields = list(map(lambda x: x.strip("\n").replace("\\N", "0"), fields))
                movie=Movie(tconst=fields[0],titleType=fields[1],primaryTitle=fields[2],originalTitle=fields[3],isAdult=fields[4],startYear=fields[5],endYear=fields[6], runtimeMinutes=fields[7],genres=fields[8])
                movie2=dict(tconst=fields[0],titleType=fields[1],primaryTitle=fields[2],originalTitle=fields[3],isAdult=fields[4],startYear=fields[5],endYear=fields[6], runtimeMinutes=fields[7],genres=fields[8])
                if movie2["isAdult"]=='1':
                    continue

                self.movies.append(movie)
                # i+=1
                # if i==100:
                #     break
        return self.movies





    def read_ratings(self,file_name: str) -> list[Movie]:
            """
            Read movie from a file into a list of Person dataclass objects.
            :param filename: The name of the file
            :return: A list of ratings
            """
            ratings = list()
            # specifying the encoding is not always necessary but some operating systems (windows) will choose the wrong encoding instead of
            # i=0
            # opening movie file for reading purpose
            with open(file_name, encoding="utf-8") as f:
                for line in f:
                    fields = line.split(',')[0].split("\t")
                    fields=list(map(lambda x:x.strip("\n").replace("\\N","0"),fields))
                    rating=Rating(tconst=fields[0],averageRating=fields[1],numVotes=fields[2])
                    movie_exist=filter(lambda movie:rating.tconst==movie.tconst,self.movies)
                    if movie_exist:
                        self.ratings.append(rating)
                    # i += 1
                    # if i == 100:
                    #     break

            return self.ratings


