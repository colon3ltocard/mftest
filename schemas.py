"""
Pydantic schemas/model to validate/parse request and replies
"""
import re
from pydantic import BaseModel, validator

VALID_YEAR_REGEX = re.compile("^(19|20)\d{2}$")  # i hate regex
MTYPES = ("", "movie", "series", "episode")


class Movie(BaseModel):
    """
    A 'simple' movie as per ...
    """

    movie_title_search_string: str
    release_year: str
    mtype: str

    @validator("release_year")
    def release_year_must_be_a_valid_year(cls, v):
        """
        we make sure the year string we receive as input is valid
        :param v:
        :return:
        """
        if v != "" and not VALID_YEAR_REGEX.match(v):  # we allow only valid years or empty value
            raise ValueError(f"Invalid year : {v}")
        return v

    @validator("mtype")
    def mtype_in_expected_vallues(cls, v):
        """
        Validated the movie type is in our tuple of allowed values
        :param v:
        :return:
        """
        if v not in MTYPES:
            raise ValueError(f"movie type {v} not in allowed list: {MTYPES}")
        return v

