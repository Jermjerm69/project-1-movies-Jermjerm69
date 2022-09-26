"""
CSCI-140/242

A program that demonstrates custom sorting a list of dataclass objects by
several fields.

Author: RIT CS
"""


from dataclasses import dataclass
import operator


@dataclass(frozen=True)
class Rating:
    """A dataclass to represent a rating that has 3 fields called tconst str, average rating and numVotes"""
    tconst:str
    averageRating:float
    numVotes:int
