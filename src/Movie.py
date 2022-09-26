"""
CSCI-140/242

A program that demonstrates custom sorting a list of dataclass objects by
several fields.

Author: RIT CS


"""


from dataclasses import dataclass
import operator




@dataclass(frozen=True)
class Movie:
    """A dataclass to represent a movie that holds all movie attributes"""
    tconst:str
    titleType:str
    primaryTitle:str
    originalTitle:str
    isAdult:bool
    startYear:int
    endYear:int
    runtimeMinutes:int
    genres:str


